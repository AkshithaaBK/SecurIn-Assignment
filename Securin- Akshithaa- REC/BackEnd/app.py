from flask import Flask
from routes import cve_routes
from database import db
import requests
from models import CVE

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cve_database.db'
db.init_app(app)
app.register_blueprint(cve_routes)

@app.cli.command()
def sync_cves():
    start_index = 0
    results_per_page = 100
    while True:
        cve_items = fetch_cves(start_index, results_per_page)
        if not cve_items:
            break
        for item in cve_items:
            cve_id = item['cve']['CVE_data_meta']['ID']
            description = item['cve']['description']['description_data'][0]['value']
            published_date = item['publishedDate']
            last_modified_date = item['lastModifiedDate']
            cve = CVE(cveID=cve_id, description=description, publishedDate=published_date, lastModifiedDate=last_modified_date)
            db.session.add(cve)
        db.session.commit()
        start_index += results_per_page
    print("CVEs synchronized successfully.")

def fetch_cves(start_index, results_per_page):
    url = f'https://services.nvd.nist.gov/rest/json/cves/2.0?startIndex={start_index}&resultsPerPage={results_per_page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['result']['CVE_Items']
    else:
        return []

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

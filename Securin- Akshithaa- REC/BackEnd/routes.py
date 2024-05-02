from flask import Blueprint, jsonify, request
from models import CVE

cve_routes = Blueprint('cve_routes', __name__)

@cve_routes.route('/cves', methods=['GET'])
def get_cves():
    cves = CVE.query.all()
    cve_list = []
    for cve in cves:
        cve_dict = {
            'cveID': cve.cveID,
            'description': cve.description,
            'publishedDate': cve.publishedDate,
            'lastModifiedDate': cve.lastModifiedDate
        }
        cve_list.append(cve_dict)
    return jsonify(cve_list)

@cve_routes.route('/cves', methods=['POST'])
def add_cve():
    data = request.get_json()
    cve = CVE(cveID=data['cveID'], description=data['description'], publishedDate=data['publishedDate'], lastModifiedDate=data['lastModifiedDate'])
    db.session.add(cve)
    db.session.commit()
    return jsonify({'message': 'CVE added successfully'})

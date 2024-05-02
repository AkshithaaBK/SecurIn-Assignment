from database import db

class CVE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cveID = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    publishedDate = db.Column(db.String(20), nullable=False)
    lastModifiedDate = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<CVE {self.cveID}>'

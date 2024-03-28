from app import db

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate = db.Column(db.String(100), nullable=False)

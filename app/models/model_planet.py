from app import db
from sqlalchemy.dialects.mysql import BIGINT

#create class that is inherited from the db.Model from SQLAlchemy
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    distance =db.Column(db.BIGINT)
    
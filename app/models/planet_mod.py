from app import db
# from sqlalchemy.dialects.mysql import BIGINT
# Where is your planet dictionary?



#create class that is inherited from the db.Model from SQLAlchemy
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    distance =db.Column(db.BIGINT)

def to_dict(self):
        planet_dict = {}
        planet_dict["id"] = self.id
        planet_dict["name"] = self.name
        planet_dict["description"] = self.description
        planet_dict["distance"] = self.distance

        return planet_dict

@classmethod
def from_dict(cls, planet_data):
   new_planet = Planet(name=planet_data["name"],
                    description=planet_data["description"],
                    distance=planet_data["distance"])

   return new_planet



    
class planets:
    def __init__(self,id,name,description,distance):
        self.id=id
        self.name=name
        self.description=description
        self.distance=distance

PLANETS = {"id":1,"name":"Mercury","description":"first planet to sun","distance":"35 million"}

def get_all_planets():
    planet_response=[]
    for planet in PLANETS:
        planet_response.append({"id":planet.id,
                                "name":planet.name,
                                "description":planet.description,
                                "distance":planet.distance,
                                })
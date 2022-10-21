class planet:
    def __init__(self,id,name,description,distance):
        self.id=id
        self.name=name
        self.description=description
        self.distance=distance

PLANETS = [
           planet(1,"Mercury","first from the sun",35000000),
           planet(2,"Venus","second from the sun",67000000),
           planet(3,"Earth","Third from the sun",93000000),
           planet(4,"Mars","Fourth from the sun",142000000)]


def get_all_planets():
    planet_response=[]
    for planet in PLANETS:
        planet_response.append({"id":planet.id,
                                "name":planet.name,
                                "description":planet.description,
                                "distance":planet.distance,
                                })
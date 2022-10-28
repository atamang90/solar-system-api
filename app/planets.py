from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self,id,name,description,distance):
        self.id=id
        self.name=name
        self.description=description
        self.distance=distance

PLANETS = [
           Planet(1,"Mercury","first from the sun",35000000),
           Planet(2,"Venus","second from the sun",67000000),
           Planet(3,"Earth","third from the sun",93000000),
           Planet(4,"Mars","fourth from the sun",142000000),
           Planet(5,"Jupiter","fifth from the sun",484000000),
           Planet(6,"Saturn","sixth from the sun",889000000),
           Planet(7,"Uranus","seventh from the sun",1790000000),
           Planet(8,"Neptune","eighth from the sun",2880000000)]

planets_bp = Blueprint("planets_bp", __name__, url_prefix ='/planets')


@planets_bp.route('', methods = ['GET'])
def get_all_planets():
    planet_response =[vars(planet) for planet in PLANETS]
    return jsonify(planet_response)


@planets_bp.route('/<id>', methods = ['GET'])
def get_one_planet(id):
    print(id)
    planet = validate_planet(id)
    return planet

def validate_planet(id):
    try:
        planet_id = int(id)
    except ValueError:
        return {"message": "Invalid planet id" },400
    
    for planet in PLANETS:
        if planet.id == planet_id:
            return vars(planet)
    
    abort(make_response(jsonify(description = "Not Found"), 404))
    
    




    


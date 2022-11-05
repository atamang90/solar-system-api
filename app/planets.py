from flask import Blueprint, jsonify, abort, make_response,request
from app.models.model_planet import Planet
from app import db
class Planet:
    def __init__(self,id,name,description,distance):
        self.id=id
        self.name=name
        self.description=description
        self.distance=distance

planets_bp = Blueprint('planets_bp', __name__, url_prefix ='/planets')

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
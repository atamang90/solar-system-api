from app import db
from app.models import planet_mod
from app.models.planet_mod import Planet
from flask import Blueprint, jsonify, abort, make_response,request


planets_bp = Blueprint('planets_bp', __name__, url_prefix ='/planets')

@planets_bp.route('', methods = ['GET','POST'])
def get_all_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance": planet.distance
            })

        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"],
                            distance=request_body["distance"])

        db.session.add(new_planet)
        db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully create", 201)



@planets_bp.route('/<id>', methods = ['GET'])
def get_one_planet(id):
    print(id)
    planet = validate_planet(id)
    return planet

def validate_planet(id):
    try:
        id = int(id)
    except ValueError:
        return {"message": "Invalid planet id" },400
    
    for planet in id:
        if planet.id == id:
            return vars(planet)
    
    abort(make_response(jsonify(description = "Not Found"), 404))

@planets_bp.route('/<id>', methods = ['POST'])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet(
                    id = request_body["id"],
                    name = request_body["name"],
                    description = request_body["description"],
                    distance = request_body["distance"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} was successfully created.",201)) 

@planets_bp.route("/<id>", methods = ["PUT"])
def update_planet(id):
    planet = validate_planet(id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance = request_body["distance"]

    db.session.commit()

    return make_response(jsonify(f"Planet #{planet.id} successfully updated"))

@planets_bp.route("/<id>", methods = ["DELETE"])
def delete_planet(id):
    planet = validate_planet(id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {planet.id} was successfully deleted", 200))
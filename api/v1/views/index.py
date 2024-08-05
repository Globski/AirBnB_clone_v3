#!/usr/bin/python3
"""
Flask route that returns the status of the API.
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/status', methods=['GET'] strict_slashes=False)
def get_status():
    """Returns the status of the API"""
    if request.method == 'GET':
        return jsonify({"status": "OK"})


def get_status():
    """
    Function to return the count of all class objects by type.
    """
    if request.method == 'GET':
        stats = {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)        
        }
        return jsonify(stats)

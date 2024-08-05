#!/usr/bin/python3
"""
Flask route that returns the status of the API.
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'] strict_slashes=False)
def get_status():
    """Returns the status of the API"""
    if request.method == 'GET':
        return jsonify({"status": "OK"})


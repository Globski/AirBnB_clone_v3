#!/usr/bin/python3
"""Flask App that serves as the backend API."""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """Teardown method to close the storage"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors by returning a JSON response
    with a message indicating the resource was not found.
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
    app.run(host="0.0.0.0", port=5000, debug=True)

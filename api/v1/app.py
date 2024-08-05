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

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)

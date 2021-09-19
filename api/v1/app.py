#!/usr/bin/python3
"""app.py to connect to API"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response



app = Flask('app')
#register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)



#declare a method to handle @app.teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def teardown_appcontext(code):
    """teardown_appcontext"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    #run your Flask server (variable app) with:
    #host = environment variable HBNB_API_HOST or 0.0.0.0 as default value
    #port = environment variable HBNB_API_PORT or 5000 as default value
    app.run(host=os.getenv('HBNH_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', 5000)))

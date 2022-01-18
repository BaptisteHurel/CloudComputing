import pytest 
from flask import Flask
import json


def configure_routes(app):

    @app.route('/')
    def index():
        return ' - - - MySQL Database `classicmodels` connection ok - - - '
    
def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.get_data() == b' - - - MySQL Database `classicmodels` connection ok - - - '
    assert response.status_code == 200



    
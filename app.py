"""A very simple RESTful API example
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

## Resources ##
# Use classes that inherit from Resource to define resources
# Let's ensure the "RouteOne" resource can handle "GET" requests


class RouteOne(Resource):
    def get(self):
        return {"data": "RouteOne: GET"}
    
    def post(self):
        return {"data": "RouteOne: POST"}


## API Routing ##
# Now add RouteOne to the api and define the endpoint - in this case it is '/'
api.add_resource(RouteOne, '/')

if __name__ == "__main__":
    app.run(debug=True)

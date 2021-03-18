"""A very simple RESTful API example
"""

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort


app = Flask(__name__)
api = Api(app)

people = {}

##
# Argument Parsing
##

# Create a RequestParser object
parser = reqparse.RequestParser()

# Specify mandatory arguments by adding arguments to routes
parser.add_argument(
    'name', type=str, help='Name of person required', required=True)


## Resources ##
# Use classes that inherit from Resource to define resources
# Let's ensure the "RouteOne" resource can handle "GET" requests
class RouteOne(Resource):
    def get(self):
        return {"data": "RouteOne: GET"}

    def post(self):
        args = parser.parse_args()
        people.update(args)
        return people


## API Routing ##
# Now add RouteOne to the api and define the endpoint - in this case it is '/'
api.add_resource(RouteOne, '/')

if __name__ == "__main__":
    app.run(debug=True)

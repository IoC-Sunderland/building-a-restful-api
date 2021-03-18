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
parser.add_argument(
    'age', type=int, help='Age of person is required', required=True)
parser.add_argument(
    'fav_food', type=str, help='Favourite food of person', required=False)


## Resources ##
class GetAllPeople(Resource):
    def get(self):
        return people


class GetAPerson(Resource):
    def get(self, name_of_person):
        return people[name_of_person]


class AddPerson(Resource):
    def post(self, name_of_person):
        args = parser.parse_args()
        people[name_of_person] = args
        return people[name_of_person]


## API Routing ##
api.add_resource(GetAllPeople, '/')
api.add_resource(GetAPerson, '/name/<string:name_of_person>')
api.add_resource(AddPerson, '/name/<string:name_of_person>')


if __name__ == "__main__":
    app.run(debug=True)

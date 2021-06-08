"""A very simple RESTful API example
"""

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

# boto3 imports
import boto3
import botocore.exceptions

# Create the dynamodb resource
dynamodb = boto3.resource('dynamodb')

app = Flask(__name__)
api = Api(app)

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
        # Get table
        try:
            TABLE = dynamodb.Table('people')
            ALL_PEOPLE = TABLE.scan()
            print(ALL_PEOPLE)
            return ALL_PEOPLE['Items']
        except:
            return 'No table found!'


class GetAPerson(Resource):
    def get(self, name_of_person):
        # Get specific item from a table
        try:
            TABLE = dynamodb.Table('people')
            PERSON = TABLE.get_item(
                Key={
                    'person-name': 'Bob'
                }
            )
            return PERSON['Item']
        except:
            return 'No person with that name found!'


class AddPerson(Resource):
    def post(self, name_of_person):
        args = parser.parse_args()
        # Get specific item from a table
        try:
            TABLE = dynamodb.Table('people')
            TABLE.put_item(
                Item={
                    'person-name': args['name'],
                    'age': args['age'],
                    'fav_food': args['fav_food']
                }
            )
            return 'Person added!'
        except:
            return 'Person not added!'


## API Routing ##
api.add_resource(GetAllPeople, '/')
api.add_resource(GetAPerson, '/name/<string:name_of_person>')
api.add_resource(AddPerson, '/name/<string:name_of_person>')


if __name__ == "__main__":
    app.run(debug=True)

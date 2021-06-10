"""A very simple RESTful API example
"""

from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json

# boto3 imports
import boto3
import botocore.exceptions

# Create the dynamodb resource
dynamodb = boto3.resource('dynamodb')

# Create the Lambda client - Note: Not a resource (as we used for DynamoDB) but a client
lambda_client = boto3.client('lambda')

# Create the S3 client
s3 = boto3.client('s3')

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


class GetOptimalHeartRateForExercise(Resource):
    def post(self, age):
        try:
            payload = {"age": age}
            # Call the userHeartRate Lambda
            result = lambda_client.invoke(FunctionName='userHeartRate',
                                          InvocationType='RequestResponse',
                                          Payload=json.dumps(payload))
            range = result['Payload'].read()
            api_response = json.loads(range)
            return jsonify(api_response)
        except:
            return "No lambda function found!"


class GetHeartRateInfoPDF(Resource):
    def get(self):
        try:
            # Get the .pdf from S3
            s3.download_file('ioc-flask-api-bucket',
                             'your-heart-rate-is23.pdf',
                             'heart-rate-info.pdf')
            
            return {"pdfdownloaded": "Yes"}, 200
        except:
            return {"pdfdownloaded": "No"}, 404


## API Routing ##
api.add_resource(GetAllPeople, '/')
api.add_resource(GetAPerson, '/name/<string:name_of_person>')
api.add_resource(AddPerson, '/name/<string:name_of_person>')
api.add_resource(GetOptimalHeartRateForExercise, '/heartrate/<int:age>')
api.add_resource(GetHeartRateInfoPDF, '/heartrateinfopdf/')


if __name__ == "__main__":
    app.run(debug=True)

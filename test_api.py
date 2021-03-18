"""Testing the very simple RESTful API

Note: Ensure Flask server is running on http://127.0.0.1:5000/
      before running this script.
"""

import requests

BASE_URL = "http://127.0.0.1:5000"


# POST Request
response = requests.post(
    BASE_URL + "/name/sue", {"name": "sue", "age": "45", "fav_food": "chips"})
print(response.text)

# Expected response

# {
#    "name": "sue",
#    "age": 45,
#    "fav_food": "chips"
# }


# GET request
response = requests.get(BASE_URL)
print(response.text)

# Expected Response

# {
#    "sue": {
#        "name": "sue",
#        "age": 45,
#        "fav_food": "chips"
#    }
# }

input()

# GET request with persons name that DOES NOT exist - will cause KeyError
response = requests.get(BASE_URL + "/name/bob")
print(response.text)

# Expected Response

# KeyError: 'bob'

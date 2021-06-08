"""Testing the very simple RESTful API

Note: Ensure Flask server is running on http://127.0.0.1:5000/
      before running this script.
"""

import requests
import simplejson as json

BASE_URL = "http://127.0.0.1:5000"

# GET request
response = requests.get(BASE_URL)

print(response.text)

# Expected Response

# [
#    {
#        'fav_food': 'Toast',
#        'person-name': 'Bob',
#        'age': '44'
#    }
# ]


# GET a specific item/person
response = requests.get(BASE_URL + "/name/Bob")
print(response.text)


# CREATE a new item
response = requests.post(BASE_URL + "/name/sue", {"name": "sue", "age": "45", "fav_food": "chips"})
print(response.status_code)
print(response.text)

# Expected Response

# 200
# "Person added!"


# DELETE an item
# ???
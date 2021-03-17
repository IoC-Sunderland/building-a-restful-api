"""Testing the very simple RESTful API

Note: Ensure Flask server is running on http://127.0.0.1:5000/
      before running this script.
"""

import requests

BASE_URL = "http://127.0.0.1:5000"

# Issue a GET Request to RouteOne
response = requests.get(BASE_URL)

# Check response is as expected
print(response.text)

# Expected response
#
# {
#    "data": "RouteOne: GET"
# }
#

# Let's try sending some data to RouteOne
response = requests.post(BASE_URL, data={"name": "jim", "age": 90, "fav_food": 'crackers'})
print(response.text)

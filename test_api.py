"""Testing the very simple RESTful API

Note: Ensure Flask server is running on http://127.0.0.1:5000/
      before running this script.
"""

import requests

BASE_URL = "http://127.0.0.1:5000"


# Let's try sending some invalid data to RouteOne
# Notice we are sending an invalid data type "age" argument here (str):
response = requests.post(
    BASE_URL, data={"name":"sue", "age": "45"})
print(response.text)

# Expected response

# {
#    "name": "sue",
#    "age": 45,
#    "fav_food": null
# }
#
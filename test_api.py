"""Testing the very simple RESTful API

Note: Ensure Flask server is running on http://127.0.0.1:5000/
      before running this script.
"""

import requests

BASE_URL = "http://127.0.0.1:5000"


# Now we have implemented the argument parser in app.py
# let's try sending some incomplete data to RouteOne
# Notice we are not sending a "name" argument here:
response = requests.post(
    BASE_URL, data={"age": 45, "fav_food": 'bread'})
print(response.text)

# Expected response

# {
#    "message": {
#        "name": "Name of person required"
#    }
# }
#
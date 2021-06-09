"""Testing the very simple RESTful API

Note: Ensure Flask server is running on http://127.0.0.1:5000/
      before running this script.
"""

import requests
import simplejson as json

BASE_URL = "http://127.0.0.1:5000"

# POST an age and get a optimal heart rate range for exercise based on age
response = requests.post(BASE_URL + "/heartrate/45")
print(response.status_code)
print(response.text)

# Expected Response

# 200
# {
#  "high": 149, 
#  "low": 122
# }

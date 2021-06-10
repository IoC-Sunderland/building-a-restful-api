"""Testing the very simple RESTful API

Note: Ensure Flask server is running on http://127.0.0.1:5000/
      before running this script.
"""

import requests
import simplejson as json

BASE_URL = "http://127.0.0.1:5000"

# GET the heart rate info .pdf doc
response = requests.get(BASE_URL + '/heartrateinfopdf/')
print(response.status_code)
print(response.text)

# Expected Response

# 200
# {
#    "downloaded": "Yes"
# }


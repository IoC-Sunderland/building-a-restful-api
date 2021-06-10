# Building a RESTful API
This project builds up a simple RESTful API over several commits.

## Architecture

<img style="width: 55vw; min-width: 330px;" src="RESTful Service.png">


## Running the project

#### Clone the repo

```git clone https://github.com/IoC-Sunderland/building-a-restful-api.git```

#### Create a virtualenv

```virtualenv my_env```

#### Activate virtualenv
```source bin/activate```

#### Install dependencies
```pip install -r requirements.txt ```

#### Rewind to intial commit
```git checkout 4569c42```

#### Run application
```python app.py```

#### Run API tests file
```python test_api.py```

Try it out! :thumbsup:

#### Checkout second commit
```git checkout 283254c```

Try it out again! :thumbsup: :thumbsup:

<br>

## Commit details

---
***Initial Commit:*** Project Start \
***Commit SHA:*** ```4569c42``` \
***Description:*** Boilerplate code to setup Flask RESTful API including:

***One Resource*** \
***One Route*** 

---
***Second Commit:*** Added test_api.py to test API and pip installed requests library \
***Commit SHA:*** ```283254c``` \
***Description:*** Added test_api.py to test API and pip installed requests library

---
***Third Commit:*** Added a POST method \
***Commit SHA:*** ```382a2bf``` \
***Description:*** Added a POST method to RouteOne resource. No data is being sent at this time.

---
***Fourth Commit:*** Sending data to POST method \
***Commit SHA:*** ```1ba0b39``` \
***Description:*** Sending some form data to the POST method and then returning it back.

---

***Fifth Commit:*** Argument Parsing \
***Commit SHA:*** ```ebf9082``` \
***Description:*** Implementing an argument parser to check data is complete.

---
***Sixth Commit:*** Invalid arguments \
***Commit SHA:*** ```5ab57f8``` \
***Description:*** Sending invalid data types where mandatory arguments have been defined using argument parser.

---
***Seventh Commit:*** More argument parsing \
***Commit SHA:*** ```f02d9cd``` \
***Description:*** Here we have provided a string argument for age which is parsed fine as it can be converted to int e.g. “45” can be parsed to 45. Also, “fav_food” argument can be omitted since it is not required by parser ```(required=False)``` and so is stored in dictionary as null.

---
***Eighth Commit:*** String arguments \
***Commit SHA:*** ```6d68025``` \
Description: Here we pass string arguments to POST and GET methods to add/retrieve users by name.

---

***Ninth Commit:*** Added DynamoDB for data persistance \
***Commit SHA:*** ```225eb54``` \
Description: Here we have added DynamoDB integration using the AWS SDK for Python (boto3) and we have included some example uses.

---

***Tenth Commit:*** Added Lambda invocation \
***Commit SHA:*** ```0b2b8a8``` \
Description: Added Lambda invocation to get optimal heart rate range for exercise.

---

***Eleventh Commit:*** Added S3 integration \
***Commit SHA:*** ```0ed94aa``` \
Description: Added S3 integration that fetches a .pdf file that gives inormation on heart rates

---

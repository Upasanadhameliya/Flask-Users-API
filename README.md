# Task - Create API


## This repository uses python=3.8 with MongoDB version v4.4.4. The api allows users to do the following things:
  1. Make a post request where one can pass in user details in JSON format with the following details:
     ID, name, mobile number, age. Eg: 
     ```
     curl --header "Content-Type: application/json" --request POST --data "{\"ID\":\"101\",\"name\":\"demo\",\"mobile number\":\"2233445566\",\"age\":\"23\"}" http://127.0.0.1:5000/
     ```
  2. Make a get request to get the details in JSON of user based on the query parameters passed in the URL.
For eg: http://127.0.0.1:5000/user/age/10 returns the details of all the users with age 10 (JSON), http://127.0.0.1:5000/user/ returns the details of all the users.

# Install
```
pip install -r requirements.txt
```

# Running the api

cd into the api directory and run:
```
python api.py
```
This would start the flask server on your localhost.


# Output

###### Fetching all users 
![Alt text](Screenshots/All_users.png?raw=true "All Users JSON")

###### Fetching specific id
![Alt text](Screenshots/Id_query.png?raw=true "ID Query JSON")

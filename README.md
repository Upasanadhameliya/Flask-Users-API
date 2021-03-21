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
This would start the flask server on your localhost. You can GET query on following urls:

```
localhost:5000/user/
localhost:5000/user/id/<give id here
localhost:5000/user/name/<give name here>
localhost:5000/user/mobile-number/<give mobile number here>
localhost:5000/user/age/<give age here>
```

The POST request can be done on following url:

```
http://127.0.0.1:5000/
```


# Output

###### Fetching all users 
![Alt text](Screenshots/All_users.png?raw=true "All Users JSON")

###### Fetching specific id
![Alt text](Screenshots/Id_query.png?raw=true "ID Query JSON")


# API Security Measures

Api security is important to prevent security threats or security breaches like:
  - Man in the middle attacks
  - Api injections
  - Distributed Denial of Service (DDoS)

Api Security can be achieved by implementing:
- Authentication : To determine the identitiy of the user.
- Authorization : Determining the resources that a user can access.


In flask we can achieve these by using:
- Using JWT : JSON Web Tokens (or JWTs) provide a means of transmitting information from the client to the server in a stateless, secure way.
- Flask-Login package : Provides a way of user authentication by means of secret keys
- Flask-Authorize package: Incorporates Access Control Lists (ACLs) and Role-Based Access Control (RBAC)

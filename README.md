# Drinks REST API

## 1. Overview
The Drinks API uses REST. It has predictable resource-oriented URLs, accepts standard HTTP requests and returns JSON responses with standard HTTP response codes. The Drinks API doesn't support bulk updates. You can only work on one object per request.

## 2. Technologies
The API was built using Python. The main dependencies used are:

flask library specifically Flask and request

``` 
from flask import Flask, request 
```

flask_sqlalchemy library specifically SQLAlchemy 

```
from flask_sqlalchemy import SQLAlchemy
```

See requirements.txt for a complete list of project dependencies.

## 3. Project Description
The project is an API for an online drink shop. The drink shop displays various drinks and their descriptions.

## 4. Installation
To install this API, use the following. Note: If you use a different OS, the code will be different.

1. Clone/download the project.

2. Create a virtual environment. 
    
    For windows users,

    ```
    python -m venv .venv
    ```

3. Activate the virtual environment.

      ```
      .venv\Scripts\Activate.ps1
      ```

4. Install the dependencies from **requirements.txt.**

    ```
    pip install -r requirements.txt
    ```

    Alternatively, the primary packages used by this project are Flask and Flask-SQLAlchemy; installing these packages with pip will also install their required dependencies.

## 5. Configuration
The API currently requires minimal configuration. Flask must be pointed to application.py, and the SQLite database is configured through Flask-SQLAlchemy.


## 6. Running the API
To run the API you can use the following

``` 
flask run 
```

If you want to run the code in debug mode, you can use flask run --debug. But you must first set the flask application you are trying to run.

``` 
flask --app application run 
```

``` 
flask run --debug 
```

OR

``` 
flask --app application run --debug 
```


## 7. API Endpoints
These are the various endpoints available in the Drinks API.

   - GET /drinks

This endpoint returns a JSON containing all drinks in the database. 
   
**Response:**
```json
{
"drinks": [
{
"description": "Tastes like grapes",
"name": "Grape Soda"
},
{
"description": "Tastes like Apples!!!!!!!!!",
"name": "Apple"
}
]
}
```

   - GET /drinks/<id\>
   
This endpoint request returns a JSON object containing information about the drink associated with the specified ID. For example, an ID of 1 returns information about the 'Apple' drink.

Assuming you call the drink with an id of 1

**Response**

```json
{
"description": "Tastes like grapes",
"name": "Grape Soda"
}
```            
    
   - POST /drinks

This endpoint request allows you to add a drink name and description to the database
        
**Request body:**

```json
{
"name": "Cola",
"description": "Delicious"
} 
```

**Reponse:**
```json
{
"id": 3 
}
```
The **id** is the ID assigned to the newly created drink

   - PATCH /drinks/<id\>

This endpoint request allows you to modify part of the drink information in the database, in this case the 'name' or 'description'.

Assuming you want to change one of the fields for a particular drink

**Request body:**
```json
{
"name": "Cola"
}

OR

{
"description": "Delicious"
}
```

**Reponse:**
```json
{
"message": "Drink modified"
}
```

   - PUT /drinks/<id\>

This endpoint request allows you to replace or update every information related to a specific drink id. 

  **Request body:**

```json
{
"name": "Cola",
"description": "Delicious"
} 
```

**Reponse:**
```json
{
"message": "Drink fully replaced"
}
```

   - DELETE /drinks/<id\>

This endpoint request allows you to delete one drink at a time from the database. 

 **Response:**
```json
{
"message" : "Drink removed"
}
```

## 8. Database
The API uses SQLite as its database and SQLAlchemy/Flask-SQLAlchemy to interact with it.  In the database, there are three columns. The id, the name, and the description. 

## 9. Testing the API
To test the API, use Postman to send an HTTP request. For requests that require info from you, add them under 'Body' in Postman

## 10. Known Limitations
The API has minimal error handling. Given the right type of edge case, the API could fail tremendously. Also, it isn't fit for production since it is being run on a development server.

**This project is intended for learning and demonstration purposes and is not production-ready.**

## 11. Future Improvements
1. Handle errors
2. Deploy the API 
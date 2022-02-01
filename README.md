# Lord-of-the-Rings-API

API for Characters and Quotes from The Lord of the Rings  
[Live Link](https://lordoftheringsapi.herokuapp.com/)

## Main API Functionalities

- User Signup
- User Login
- Get All Characters (with Pagination)
- Get All Quotes from a Character (with Pagination)
- User save a Character as Favorite
- User save a Quote with its Character information as Favorite
- User retrieve all her favorited items
- User unfavorite an item

## Tech Stacks

- Python
- Flask
- Postgres DB

## How to Run the Project

Clone the project repository

```
git clone https://github.com/Timothy-py/Lord-of-the-Rings-API.git

```

Enter the project folder and create a virtual environment

```
$ cd Lord-of-the-Rings-API/
$ virtualenv venv
```

Activate the virtual environment

```
$ source venv/bin/activate
```

Install all requirements

```
$ pip install -r requirements.txt
```

Create an environment file in the source directory

```
$ touch .env
```

Set the following environment variables in the .env file

```
SECRET_KEY="dev"
SQLALCHEMY_DATABASE_URI=sqlite://lord_of_the_rings_db
API_KEY=VEY3rmUUcMG2gwhoTnMD
JWT_SECRET_KEY=JWT_SECRET_KEY
```

Create the database (run the following commands)

```
$ flask shell
$ from src.model import db
$ db.create_all()
```

Run the application

```
flask run
```

---

\*\* The Swagger documentation can be accessed on the browser - http://localhost:5000/

###### _contact me @ adeyeyetimothy33@gmail.com_

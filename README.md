# Hello-Books-API

Hello-Books-APi is a library management API. It help in management and tracking of books and users who interact with the library's books. The API also enable new users to register while existing users can login. Users can also reset their password and borrow books.
The API functionality and the respective endpoints include the following:  

- To view documentation click [here](https://hellobookapi.docs.apiary.io/).   

| Functionality              |Authorized|
|----------------------------|---------------------
|Add a book                  | Admin only               
|Modify a book’s information | Admin only
|Remove a book               | Admin only
|Retrieves all books         | Everybody
|Get a book                  | Everybody
|Borrow a book               | logged in User and Admin
|Register a user             | Everybody
|Upgrade a user to admin     | Admin only
|Get registered users        | Admin only
|Login a user                | Registered user
|Logout a user               | Loggged in user
|Reset a user Password       | Registered user
|Borrow a books              |Logged in user
|Return a books              |Logged in user
|Get user borrowing history  |Logged in user

#### Running and Testing of the API

**Prequisites**
```
Python - version 3.6.4
Postgress database
GraphQL- To run various endponts
```
**Installing**   

Perform the following simple steps:   
- Open git and navigate to directory yo which to run the app from.
- Git clone the this repository using either.
  - Using SSH:
    
    ``git@github.com:sam-karis/Hello-Book-API-GraphQL.git``
  
  - Using HTTP:
    
    ``https://github.com/sam-karis/Hello-Book-API-GraphQL.git``

- Set up a virtual eniviroment for reference click [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

- Activate the virtualenv on your terminal

- Now install the apps dependencies by running `pip install -r requirements.txt`

- Create databaseand set global variables on the terminal  
  - For database set `DATABASE_URL= 'yourdatabaseurl'`
  - For email sending   
  `Email='defaultmail@example.com'`   
  `Username='yourusername'`   
  `Password='dmy_password'`

- Run manage.py to create database tables as below   
    `python manage.py db init`   
    `python manage.py db migrate`   
    `python manage.py db upgrade`


- Set the following configuration on terminal to run the app``FLASK_CONFIG=development, FLASK_APP=run.py``
- Then run ``flask run`` to launch the localhost.
- Lastly with the app running access the endpoints using postman.

While working with postman use the following attributes:
- For adding and editing books - ``title``, ``description``, ``edition``, ``author``
- User registration - ``name``, ``email`` ,``password``
- User login - ``email ``,  ``password``
- User logout, borrow  and returnbook,  - ``email``
- User reset password - ``email``,  ``new_password``

**Tests**
Hello-Books-API has automated test(unittest) to check if it the endpoints work as expected. To run the tests activate the virtual environment and then run `nosetests --with-coverage`

**To contribute to this work**

Fork the repository from links shared above and make a pull request.
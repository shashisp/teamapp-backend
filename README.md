
### How to Setup teams backend

###### Create virutal environment
```
virtualenv env
source env/bin/activate
```
###### Install Dependencies
```
pip install -r requirements.txt
```
### How to run the project
```
python manage.py runserver
```

### How to Test APIs
```
1. Users list API
    curl -X GET http://127.0.0.1:8000/users/
    [
        {
            "pk": 1,
            "first_name": "Bruce",
            "last_name": "New last name",
            "phone": "5122168404",
            "email": "batman@gotham.com",
            "is_staff": true
        },
    ]

2. Add User API: Make POST requests to users API (http://127.0.0.1:8000/users/) with data in request body
    eg:
    curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/users/ -d '{"first_name": "Cartman", "last_name": "New last name", "phone": "5122168404", "email": "new_user@gmail.com", "is_staff": true  }'

{"pk":12,"first_name":"Cartman","last_name":"New last name","phone":"5122168404","email":"new_user@gmail.com","is_staff":true}


3. Update User API: Make PUT requests to user detailed API (http://127.0.0.1:8000/users/<unique_pk_value>/)
    eg:
    curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/users/12/ -d '{"first_name": "Kenny", "last_name": "last name",  "is_staff": false  }'

    {"pk":12,"first_name":"Kenny","last_name":"last name","phone":"5122168404","email":"new_user@gmail.com","is_staff":false} 

4. Delete User API: Make DELETE requests to user detailed API
(http://127.0.0.1:8000/users/<unique_pk_value>/)
eg:
    curl -X DELETE http://127.0.0.1:8000/users/12/
```

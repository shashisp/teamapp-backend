
### How to install dependencies

###### Create virutal environment
```
virtualenv env
source env/bin/activate
```
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

2. Add User API
    curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/users/ -d '{"first_name": "Cartman", "last_name": "New last name", "phone": "5122168404", "email": "cartman@gmail.com", "is_staff": true  }'
    
    
```

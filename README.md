# Crud-API-Django
This is a Basic Crud - API based Application which has a feature of Authentication and Authorizatin.

```shell

python -m venv venv
venv\Scripts\activate
. venv/bin/activate
pip3 install -r requirements.txt
python manage.py migrate
python manage.py runserver

```

For create API:Use Post Method
```
http://127.0.0.1:8000/api/v1/students/
```
<br/>

For update API:Use Patch Method
```
http://127.0.0.1:8000/api/v1/students/?id=1
```
<br/>

For Delete API: Use Delete Method
```
http://127.0.0.1:8000/api/v1/students/?id=1
```
<br/>

For GET API : Use Get API to fetch all records
```
http://127.0.0.1:8000/api/v1/students/
```
<br/>

Json Body Example:
```
{
    "name":"pratuysh",
    "degree":"B.Tech",
    "age":22,
    "sex":"male",
    "address":"india"
}
```

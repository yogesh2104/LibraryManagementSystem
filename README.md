# LibraryManagementSystem

## Install Requirement.txt file
```
pip install -r requirements.txt
```
## After Installing
## Add database details in settings.py file  
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #for mysql database
        'NAME': 'true_value_access', # database name
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306' #database port 
    }
}
```
# Afert Adding database details in settings.py make Migrations and Migrate
```
python manage.py makemigrations
```
```
python manage.py migrate
```
## After Migrate Run Project On Local Machine
```
python manage.py runserver
```
## Project on local machine on http://127.0.0.1:8000 this port base end point redirect to swagger UI documentation
![Documentation Screenshot](https://github.com/yogesh2104/LibraryManagementSystem/blob/main/DocPNG.png)


## Api Endpoint
```
        'Login':'login/',
        'User Data':'user/',
        'register':'register/',
        'logout':'logout/',
        'Documantation':'doc/',
        'List':'/book-list',
        'Details View':'/book-details/<int:id>',
        'Add Book':'/book-add/',
        'Update':'/book-update/<int:id>',
        'Dalete':'/book-detete/<int:id>',
```

## For Admin Panel Create superuser

```
python manage.py createsuperuser
```
## Enter username and password then restart server and run
```
python manage.py runserver
```

## And type this url on your browser http://127.0.0.1:8000/admin 

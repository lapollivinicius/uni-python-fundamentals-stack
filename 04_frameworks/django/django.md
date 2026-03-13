# Working with django

Django is a framework in python to web applications, it have features like ORM, Templates to frontend, routes and some else.

To start a django project, use this on venv:

```
django-admin startproject <project-name>
```

django will create a environment with some libs and tools to create application

it will create a file called manage.py, it will important to manage our application

*settings.py* -> used to defination and setup of project

*urls.py* -> used to define routes and urls to our project

## RUN DJANGO

Django have a server that need to be executed to running our application

use this, to run:

```
python manage.py runserver
```

and your application will be running on your localhost at port 8000

## CREATE APP WITH DJANGO

Now, you have create your own app/project using django, to create your app, use:

```
python manage.py startapp <app-name>
```

## MIGRATE

fisrt, you need to create your models in your app, then you need to migrate your database, use this:

```python manage.py makemigrations
```

so, after, you will need to migrate your database, use this:

```python manage.py migrate
```

to work with database, you can use the shell of django, use this:

```python manage.py shell
```
see some commands to work with database:

```python
from <app-name>.models import <model-name>

# create new object
new_object = <model-name>(field1=value1, field2=value2)
new_object.save()

# get all objects
objects = <model-name>.objects.all()

# get object by id
object = <model-name>.objects.get(id=1)

# show all objects
for obj in objects:
    print(obj.field1, obj.field2)

# update object
object.field1 = new_value
object.save()

# delete object
object.delete()
```

## DJANGO ADMIN

Django have a admin panel, to access it, you need to create a superuser, use this:

```python manage.py createsuperuser
```

after, you can access the admin panel at http://localhost:8000/admin/ and login with your superuser credentials
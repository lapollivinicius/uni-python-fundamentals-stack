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



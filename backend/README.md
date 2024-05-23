# Backend Application powered by Django Framework and Python Programming language

## Prerequisites

* Git
* Python 3
* Django 5

This project has been created with Python version 3.10.12 and Django version 5.0.4 on a machine with Ubuntu OS version 22.04.1

## Installation

### Git

You will need this Source Code Management Tool to download the application from the git repository.

```shell
sudo apt install git-all
git --version
```
If Git is installed, you should see the version of your installation:

git version 2.34.1

For other Operating systems see the following link:

https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### Install virtualenv
```shell
python -m pip --version
python -m pip install virtualenv
```

### Create a virtual environment 
Inside the folder where later, you will clone the source code for this project run the following commands: 
```shell
python -m venv packtDjango-venv
```

### Activate/use the virtual environent
```shell
source packtDjango-venv/bin/activate (Linux)
packtDjango-venv\Scripts\activate (Windows)
```

### Python programming language

```shell
sudo apt update
sudo apt install python3
python3 --version
```
If Python is installed, you should see the version of your installation:

Python 3.10.12

For other Operating systems see the following link:
https://kinsta.com/knowledgebase/install-python/

### Django framework

```shell
python -m pip install Django
python -m django --version
python -m pip install django-environ
```
If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.

For other Operating systems see the following link:
https://docs.djangoproject.com/en/5.0/topics/install/

### Django Behave integration

```shell
python -m pip install behave-django
behave --version
```
If Behave is installed, you should see the version of your installation:

behave 1.2.6

### Other Testing tools

```shell
python -m pip install parameterized
```

## Project Download
You can clone the github repository containing the source code of this book:
```shell
git clone https://github.com/PacktPublishing/Full-Stack-Web-Development-with-Django-and-Angular.git 
```

## Project initialization (optional)
Only in case you want to start your own project (not necessary for this tutorial) type the following command:

```shell
django-admin startproject packtDjangoProject
```
## Run Postgres Database
Install docker in your machine

Inside the docker folder type the following command:

```shell
docker-compose -f docker-compose.yml up -d
```

## Run Backend Application
Inside packtDjangoBackend folder type the following command:

```shell
python manage.py runserver
```

You should see something like:

Django version 5.0.4, using settings 'packtDjangoBackend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

## Verify Project is running
```shell
curl localhost:8000
```
Optionally open your prefered web browser at the URL http://localhost:8000

## Create a new Application

To create your app, make sure you’re in the same directory as manage.py and type this command:

```shell
python manage.py startapp packtDjangoApp
```

## Migrate the Database 
```shell
python manage.py makemigrations packtDjangoApp
```
default database: sqlite3
```shell
python manage.py migrate --database=sqlite3-packtdjango
```
postgres-packtdjango: postgress
```shell
python manage.py migrate --database=postgres-packtdjango
```

## Execute tests

To automatically test your app, make sure you’re in the same directory as manage.py and type this command:

```shell
python manage.py test
```

## Execute BDD tests
```shell
python manage.py behave
```
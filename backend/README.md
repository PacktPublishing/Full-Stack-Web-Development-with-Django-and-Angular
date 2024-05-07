# Backend Application Powered by Django Framework and Python Programming language

## Prerequisites

* Python 3
* Django 5

This project has been created with Pyton version 3.10.12 and Django version 5.0.4

## Installation

### Django framework

```shell
python -m pip install Django
python -m django --version
```
If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.

## Project initialization
Only in case you want to start your own project (not necessary for this tutorial)type the following command:

```shell
django-admin startproject packtDjangoProject
```

## Run Backend Application
Inside packtDjangoBackend folder type the following command:

```shell
python manage.py runserver
```

You should see something like 

```shell
Django version 5.0.4, using settings 'packtDjangoBackend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

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
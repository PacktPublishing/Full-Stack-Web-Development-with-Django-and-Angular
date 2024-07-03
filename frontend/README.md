# Frontend Application Powered by Angular Framework and Typescript Programming language


# Prerequisites

* Git
* Node 20.5.0
* Anglular CLI 16.1.6

This project has been created with [Angular CLI](https://github.com/angular/angular-cli) version 16.1.6 and Node 20.5.0 on a machine with Ubuntu OS version 22.04.1

## Installation

### Git

You will need this Source Code Management Tool to download the application from the git repository.

```shell
$ sudo apt install git-all
$ git --version
```
If Git is installed, you should see the version of your installation:

git version 2.34.1

For other Operating systems see the following link:

https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

### Install node and Angular CLI
```shell
$ brew install node@20
$ echo 'export PATH="/opt/homebrew/opt/node@20/bin:$PATH"' >> ~/.zshrc
$ npm install -g @angular/cli@16
$ ng version
```
If Angular is installed, you should see the version of your installation:

Angular CLI: 16.1.6
Node: 20.5.0
Package Manager: npm 9.8.0
OS: linux x64

## Project Download
You can clone the github repository containing the source code of this book:
```shell
$ git clone https://github.com/PacktPublishing/Full-Stack-Web-Development-with-Django-and-Angular.git 
```

## Project Installation
You can install the project with the following command:
```shell
$ npm install
```

## Project and application initialization (optional)
Only in case you want to start your own project (not necessary for this tutorial) type the following command:

```shell
$ ng new angularpackt-ui --prefix apui --routing
```
## Run Postgres Database and DRF backend app.
Install docker in your machine

Inside the docker folder type the following command:

```shell
$ docker-compose -f docker-compose.yml up -d
```

## Run Frontend Application
Inside frontend folder type the following command:

```shell
$ ng serve
```

You should see something like:

```
** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **
✔ Compiled successfully.
```

The app will automatically reload if you change any of the source files.

## Verify Project is running
```shell
$ curl localhost:4200
```
Optionally open your prefered web browser at the URL http://localhost:4200

## Execute BDD tests

To automatically test your app, use this command:

```shell
$ ng test
```
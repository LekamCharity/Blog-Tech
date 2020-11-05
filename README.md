# Blog-TECH

## Author

Lekam Charity

## Description

Blog-Tech is an application where users can view blogs,leave comments,submit their blogs .

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* View the blog posts submitted.
* Comment on blog posts.
* View the most recent posts
* Alerted when a new post is made by joining a subscription.

## Live link to the website 
  ``` https://blogwithlekam.herokuapp.com/```

## Set-up and Installation

# Software Requirements
    - Python 3.8
    - PostgreSQL DMS

### Clone the Repo
Run the following command on the terminal:
* `git clone https://github.com/LekamCharity/Blog-Tech`
*  cd Blog-Tech
Install [Postgres](https://www.postgresql.org/download/)
Install [Python](https://www.python.org/downloads/)

### Create a Virtual Environment
Run the following commands in the same terminal:
* ```python3.8 -m venv --without-pip virtual```
* ```curl https://bootstrap.pypa.io/get-pip.py | python```
* ```source virtual/bin/activate```

### Database
Quickly create a database where your data is going to be persistent .
```
psql
you=#  CREATE DATABASE blogtechnology;
```

```bash
SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://username:password@localhost/blogtechnology'
SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3.8 manage.py server` 


## Technologies used
    - Python 3.8
    - HTML
    - Heroku
    - Postgresql


## Contact Information 

If you have any question or contributions, please email me at [lekamcharity@gmail.com]

### License
  [MIT](https://github.com/LekamCharity/Blog-Tech/blob/master/License) Copyright (c) 2020 Lekam Charity


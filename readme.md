#Rest API programming test

This project is created using Django Framework, 
and using pipenv as a package versioning and environment isolator

##How To Run:

`pipenv install` -> To Install project requirements

`pipenv shell python manage.py migrate` -> To Create Databases tables and info

`pipenv shell python manage.py runserver` -> To Run project

`pipenv shell python manage.py test` -> To Run unit tests


##Exposed Endpoints

| Type | Endpoint       | Needs Auth | Description            |
|------|----------------|------------|------------------------|
|  Get | jobs/          | No         | list all existing jobs |
|  Get | jobs/\<status> | No         | get jobs by status     |
|  Get | jobs/          | Yes        | creates new job        |


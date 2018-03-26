# selfiegram-api

## Install
```sh
$ git clone https://github.com/moisesdelacruz/selfiegram-api.git

$ cd selfiegram-api/

# create .env file
$ touch .env

# build docker image
$ docker-compose build

# run docker image
$ docker-compose up
```

## Commands aditionals
```sh
# Make migrations
docker-compose run web python manage.py makemigrations

# Apply migrations
docker-compose run web python manage.py migrate

# Install python dependencies
# access to docker container web and run:
pip install <dependencies>
pip freeze -l > requirements.txt

# Access to container in execution
docker exec -it <id_container> /bin/bash
```

## .env file content
```sh
# Django App
SECRET_KEY=

# Data Base Postgres
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```

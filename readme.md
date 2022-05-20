
# Automate Contact Form Submission

## installation

```shell

pip3 install -r requirements.txt 

```

## setup

```shell

export FLASK_ENV=development

export FLASK_APP=automation.main

```

## run App

```shell

flask run --host=0.0.0.0

```

## run celery worker

```shell

celery --app automation.server.tasks.celery worker --loglevel=info

```
## start server

```shell
run start_server.sh
```

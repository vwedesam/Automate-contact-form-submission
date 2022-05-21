
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

## PROD SCRIPT
```shell

from server.main.automation.script import AutomateForm


PATH = "./chromedriver.exe"
url = ""

form = AutomateForm(PATH, url)

form.waitForTitle()

firstname = 'sam'
lastname = 'wisdom'
phone = ""
email = ""
message = ""

form.find_and_set_field('name', f"{lastname} {firstname}", '_email')

form.find_and_set_field('fullname', f"{lastname} {firstname}", '_email')

form.find_and_set_field('first', f"{firstname}", '_email')

form.find_and_set_field('firstname', f"{firstname}", '_email')

form.find_and_set_field('lastname', f"{lastname}", '_email')

form.find_and_set_field('last', f"{lastname}", '_email')

form.find_and_set_field('phone', phone, '_phone')

form.find_email_and_set_field(email, '_email')

form.find_messaage_box_and_set_field(message, '_message')


```

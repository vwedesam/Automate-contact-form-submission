
# Automate Contact Form Submission
The `scripts.py` contains re-usable class methods that makes form automation easy 

## Setup
1. create a virtual env
2. add the required env vars
3. download chromedriver (https://chromedriver.chromium.org/downloads)

`chromedriver version should be the same as the chrome installed on your PC `

## installation

```shell
pip3 install -r requirements.txt 
```

## ENV
```shell
export FORM_URL="http://localhost:5000"
export FLASK_ENV=development
export FLASK_APP=automation.main
```

## run App
`This gives you a form to test the automation scripts`
```shell
flask run --host=0.0.0.0
/// shell
run start_server.sh
```

## RUN TEST SCRIPT
```shell
py automation/test.py
```

# Captcha Automation Coming Soon !!!

# Celery integration Coming Soon !!!
## run celery worker
```shell
celery --app automation.server.tasks.celery worker --loglevel=info
```

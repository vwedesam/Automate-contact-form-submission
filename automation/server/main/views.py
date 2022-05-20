from flask import (
    Blueprint, flash, jsonify, redirect, render_template, request, session, url_for
)
from celery.result import AsyncResult
from selenium.webdriver.common.by import By
from ..tasks import create_task
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

main_blueprint = Blueprint('auth', __name__, url_prefix='/')


@main_blueprint.route("/", methods=["POST", "GET"])
def home():
    return render_template('form.html')


# Get form inputs
@main_blueprint.route("/automate", methods=["POST"])
def automate_task():
    first_name = request.form.get("name")
    surname = request.form.get("surname")
    email = request.form.get("email")
    need = request.form.get("need")
    message = request.form.get("message")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url: str = "https://www.nacsllc.org/contact"

    # Selenium
    # path: str = "../../chromedriver"
    # driver = webdriver.Chrome(path)
    driver.maximize_window()
    driver.get(url)

    # name_field = driver.find_element(by=By.ID, value="FullName")
    # name_field.send_keys(first_name)
    #
    # email_field = driver.find_element(by=By.ID, value="Email")
    # email_field.send_keys(email)
    #
    # phone_field = driver.find_element(by=By.ID, value="Phone")
    # phone_field.send_keys("08022222222")
    #
    # comment = driver.find_element(by=By.ID, value="QuestionsComments")
    # comment.send_keys(need)
    #
    # find_us = driver.find_element(by=By.ID, value="FindUs")
    # find_us.send_keys("Friend")
    #
    # button = driver.find_element(by=By.ID, value="Submit")
    # button.click()

    # print(form.text)
    # name.send_keys(first_name)
    # name.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

    return f"AUTOMATING... {first_name, surname, email, need, message}"


@main_blueprint.route("/tasks", methods=["POST"])
def run_task():
    content = request.json
    task_type = content["type"]
    task = create_task.delay(int(task_type))
    return jsonify({"task_id": task.id}), 202


@main_blueprint.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return jsonify(result), 200

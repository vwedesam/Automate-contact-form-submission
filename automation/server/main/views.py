from flask import (
    Blueprint, flash, jsonify, redirect, render_template, request, session, url_for
)
from celery.result import AsyncResult
from ..tasks import create_task

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

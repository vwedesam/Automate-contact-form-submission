from flask import Flask
from dotenv import load_dotenv
from .server.main import views
from .server import config

load_dotenv()  # take environment variables from .env.

app = Flask(__name__, template_folder="./server/templates")

# config Mailer
config.mailConfig(app)

# register view
app.register_blueprint(views.main_blueprint)



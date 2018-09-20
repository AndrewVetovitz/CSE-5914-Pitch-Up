from flask import Flask
from controllers.user import user_blueprint
from controllers.reports import report_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)

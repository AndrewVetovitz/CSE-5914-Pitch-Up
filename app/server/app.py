from flask import Flask
from controllers.user import user_blueprint
from controllers.report import report_blueprint
import sys

app = Flask(__name__)

app.register_blueprint(user_blueprint)

if __name__ == "__main__":

    app.run(debug=True, port=5000)

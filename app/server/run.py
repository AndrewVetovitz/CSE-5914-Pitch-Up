import os
from os.path import join
from os.path import dirname
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from authlib.flask.client import OAuth
from six.moves.urllib.parse import urlencode

from database import db
from config import SQLITE_DB_LOCATION

from controllers.user import user_blueprint
from controllers.pitch import pitch_blueprint
# from controllers.report import report_blueprint

from helpers.authenticate import AuthError

################################################################################
# Application driver
#
#   To run application from shell: python app.py
#
################################################################################

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config["UPLOAD_FOLDER"] = os.getenv("UPLOAD_FOLDER")

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB_LOCATION
    db.init_app(app)

    # Views/Blueprints
    app.register_blueprint(user_blueprint)
    app.register_blueprint(pitch_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='localhost', port=5000)

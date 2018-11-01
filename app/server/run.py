import os, sys
from os.path import join, dirname
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from authlib.flask.client import OAuth
from six.moves.urllib.parse import urlencode
from flask_cors import CORS

from database import db
from config import get_environment_config

from controllers.user import user_blueprint
from controllers.pitch import pitch_blueprint
from controllers.pitch_try import pitch_try_blueprint
# from controllers.report import report_blueprint

from helpers.authenticate import AuthError

################################################################################
# Application driver
#
#   To run application from shell: python app.py
#
################################################################################

from flask import Flask

def create_app(environment='DEVELOPMENT'):
    ''' Create the application with the provided enviornment variable.
        environment: 'DEVELOPMENT', 'TESTING', 'PRODUCTION'
            - Defaults to 'DEVELOPMENT' 
    '''

    env_config = get_environment_config(environment)

    app = Flask(__name__)

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    # Apply configurations
    if not env_config:
        print("[!] There was an error configuring the application. Exiting.")

    app.config["UPLOAD_FOLDER"] = os.getenv("UPLOAD_FOLDER")
    app.config['SQLALCHEMY_DATABASE_URI'] = env_config['RDBMS_DATABASE_URI']
    app.config['TESTING'] = env_config['TESTING']

    # Database
    db.init_app(app)

    # Views/Blueprints
    app.register_blueprint(user_blueprint)
    app.register_blueprint(pitch_blueprint)
    app.register_blueprint(pitch_try_blueprint)
    
    # CORS
    CORS(app)

    return app

if __name__ == "__main__":

    # Load the environment, checking first passed in as CLI argument, 
    # then global variable, then default.
    # TODO this needs to eventually be a simple function call to parse args,
    # so we can have dynamic host names, etc.
    env = False
    if len(sys.argv) > 1:
        env = sys.argv[1]

    if not env:
        env = os.getenv('APP_ENVIRONMENT', 'DEVELOPMENT')

    print("[~] Starting application in", env, "environment.")

    app = create_app(env)
    app.run(debug=True, host='localhost', port=5000)

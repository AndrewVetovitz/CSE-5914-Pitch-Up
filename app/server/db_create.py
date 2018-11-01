################################################################################
# Create the database with all implemented models
#
################################################################################

import os, sys
from datetime import datetime

from database import db
from models.pitch import Pitch
from models.pitch_try import PitchTry
from models.user import User
from models.document import Document
from run import create_app

def create_database(environment):
    ''' Create a database for the given environment '''

    flask_app = create_app(environment)
    flask_app.app_context().push()

    db.create_all()


def drop_database(environment):
    ''' Delete a database for the given environment '''

    flask_app = create_app(environment)
    flask_app.app_context().push()

    db.drop_all()

if __name__ == "__main__":

    env = 'DEVELOPMENT'
    if len(sys.argv) > 1:
        env = sys.argv[1]
    
    create_database(env)

    print("[~] Successfully created a database for the", env, "environment.")

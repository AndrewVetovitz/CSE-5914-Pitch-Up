################################################################################
# Create the database with all implemented models
#
################################################################################

from database import db
import models

from app import create_app

flask_app = create_app()
flask_app.app_context().push()

db.create_all()

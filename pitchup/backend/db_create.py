################################################################################
# Create the database with all implemented models
#
################################################################################

from app.database import db
import app.models

from run import create_app

flask_app = create_app()
flask_app.app_context().push()

db.create_all()
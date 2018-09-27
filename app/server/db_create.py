################################################################################
# Create the database with all implemented models
#
################################################################################

from database import db
from models.pitch import Pitch
from models.pitch_try import PitchTry
from models.user import User

from run import create_app

flask_app = create_app()
flask_app.app_context().push()

db.create_all()

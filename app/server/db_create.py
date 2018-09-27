################################################################################
# Create the database with all implemented models
#
################################################################################

from database import db
from models.pitch import Pitch
from models.pitch_try import PitchTry
from models.user import User
from datetime import datetime

from run import create_app

flask_app = create_app()
flask_app.app_context().push()

db.create_all()

# Create some dummy data
user = User(name = "Chris Ellis", email = "chris@bingoogle.com", password="123456")
db.session.add(user)
db.session.commit()
print("Added:", user)

pitch = Pitch(name = "Amazing new speaker technology", user_id = user.id)
db.session.add(pitch)
db.session.commit()
print("Added:", pitch)


pitch_try = PitchTry(pitch_id=pitch.id, transcription="Hey there you're such shit", duration=12)
db.session.add(pitch_try)
db.session.commit()
print("Added:", pitch_try)
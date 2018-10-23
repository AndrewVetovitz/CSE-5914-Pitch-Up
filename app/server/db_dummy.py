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

def add_dummy_data(environment):
    ''' Create dummy data for the given environment
    
    '''

    flask_app = create_app(environment)
    flask_app.app_context().push()


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

    pitch_try = PitchTry(pitch_id=pitch.id, transcription="Hey i am interested in audio engineering how about you there are some cool things we can do with it", duration=20)
    db.session.add(pitch_try)
    db.session.commit()
    print("Added:", pitch_try)
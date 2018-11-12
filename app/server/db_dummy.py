################################################################################
# Create the database with all implemented models
#
################################################################################

import os, sys, csv
from datetime import datetime

from database import db
from models.pitch import Pitch
from models.pitch_try import PitchTry
from models.user import User
from run import create_app

import settings

DUMMY_DATA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'database', 'dummy_data')

def add_dummy_data(environment):
    ''' Create dummy data for the given environment'''

    try:
        flask_app = create_app(environment)
        flask_app.app_context().push()

        # Create some useful dummy data for demos
        user = User(name = "Chris Ellis", username="chrisy", email = "chris@bingoogle.com", password="123456")
        db.session.add(user)
        db.session.commit()
        print("Added:", user)

        # Audio engineering
        pitch = Pitch(name = "Amazing new speaker technology", user_id = user.id)
        db.session.add(pitch)
        db.session.commit()
        print("Added:", pitch)

        pitch_try = PitchTry(pitch_id=pitch.id, transcription="Hey there I am doing research for new audio technologies are you interested in hearing more", duration=8)
        db.session.add(pitch_try)
        db.session.commit()
        print("Added:", pitch_try)

        pitch_try = PitchTry(pitch_id=pitch.id, transcription="Hey i am interested in audio engineering how about you there are some cool things we can do with it", duration=12)
        db.session.add(pitch_try)
        db.session.commit()
        print("Added:", pitch_try)

        pitch_try = PitchTry(pitch_id=pitch.id, transcription="My name is Chris and I work with audio technologies we have new research that is paving the way for some exciting breakthroughs that will push the boundaries of audio engineering as we know it today", duration=20)
        db.session.add(pitch_try)
        db.session.commit()
        print("Added:", pitch_try)

        # Pet sitting service
        # pitch = Pitch(name = "Pet sitting service", user_id = user.id)
        # db.session.add(pitch)
        # db.session.commit()
        # print("Added:", pitch)

        # pitch_try = PitchTry(pitch_id=pitch.id, transcription="Hey I run a pet sitting service. If you have a dog or cat i can pet sit it", duration=8)
        # db.session.add(pitch_try)
        # db.session.commit()
        # print("Added:", pitch_try)

        # pitch_try = PitchTry(pitch_id=pitch.id, transcription="I am a pet sitter. Call me if you need anyone to watch your pets! My number is 123 456 7829", duration=10)
        # db.session.add(pitch_try)
        # db.session.commit()
        # print("Added:", pitch_try)

        # pitch_try = PitchTry(pitch_id=pitch.id, transcription="I am a highly-rated pet sitter. I love watching pets and treat them like family. You can count on me if you ever are in need of a pet-sitter. my email is joe@pet.com", duration=13)
        # db.session.add(pitch_try)
        # db.session.commit()
        # print("Added:", pitch_try)

        ### User: Dummy Data
        ##############################################
        # print("Adding user data.")
        # with open(os.path.join(DUMMY_DATA_PATH, 'user.csv'), newline='') as csvfile:
        #     reader = csv.DictReader(csvfile)
        #     for row in reader:
        #         user = User(name = row['name'], email = row['email'], password="123456")
        #         db.session.add(user)
                
        db.session.commit()

    except Exception as e:
        print(e)
        print("[!] An error occurred while trying to add dummy data. Exiting.")
        exit()


if __name__ == "__main__":

    env = 'DEVELOPMENT'
    if len(sys.argv) > 1:
        env = sys.argv[1]
    
    add_dummy_data(env)

    print("[~] Successfully added dummy data in the database for the", env, "environment.")


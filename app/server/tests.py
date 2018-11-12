import os
import unittest
import settings

from run import create_app
from database import db
from models.user import User
from models.pitch import Pitch
from models.pitch_try import PitchTry
from db_create import create_database, drop_database
from db_dummy import add_dummy_data

env = 'TESTING'

class allTests(unittest.TestCase):
    ''' User entity test suite '''

    def setUp(self):
        self.app = create_app(env)
        self.client = self.app.test_client()
        db.init_app(self.app)
        
    def tearDown(self):
        db.session.remove()

    # Users
    def test_user_add(self):
        new_user = User("Joey Smith", "joe@joe.com", "rofl1234")
        db.session.add(new_user)
        db.session.commit()
        check_user = User.query.filter_by(id=new_user.id).first()

        self.assertEqual(check_user, new_user)

    def test_user_delete(self):
        new_user = User("Joey Smithzor", "deleteme@joe.com", "rofl1234")
        db.session.add(new_user)
        db.session.commit()
        check_user = User.query.filter_by(id=new_user.id).first()
        db.session.delete(check_user)
        db.session.commit()
        deleted_user = User.query.filter_by(id=check_user.id).first()

        self.assertFalse(deleted_user)

    # Pitches
    def test_pitch_add(self):
        new_pitch = Pitch(user_id=1, name="Widgets and Stuffs")
        db.session.add(new_pitch)
        db.session.commit()
        check_pitch = Pitch.query.filter_by(user_id=1, name="Widgets and Stuffs").first()

        self.assertEqual(new_pitch, check_pitch)

    def test_pitch_delete(self):
        new_pitch = Pitch(user_id=1, name="Cool things and Cooler things")
        db.session.add(new_pitch)
        db.session.commit()
        check_pitch = Pitch.query.filter_by(user_id=1, name="Cool things and Cooler things").first()
        db.session.delete(check_pitch)
        db.session.commit()
        deleted_pitch = Pitch.query.filter_by(id=check_pitch.user_id, name="Cool things and Cooler things").first()

        self.assertFalse(deleted_pitch)

    # Pitch Tries
    def test_pitch_try_add(self):
        trans = "Hey there I am giving you a pitch and pitches"
        new_pitch = Pitch(user_id=1, name="Widgets and Stuffs")
        db.session.add(new_pitch)
        db.session.commit()
        new_pitch_try = PitchTry(pitch_id=new_pitch.id, transcription=trans, duration=10)
        db.session.add(new_pitch_try)
        db.session.commit()
        check_pitch_try = PitchTry.query.filter_by(pitch_id=new_pitch.id).first()

        self.assertEqual(new_pitch_try, check_pitch_try)

    # def test_pitch_try_delete(self):
    #     new_pitch = Pitch(user_id=1, name="Cool things and Cooler things")
    #     db.session.add(new_pitch)
    #     db.session.commit()
    #     check_pitch = Pitch.query.filter_by(user_id=1, name="Cool things and Cooler things").first()
    #     db.session.delete(check_pitch)
    #     db.session.commit()
    #     deleted_pitch = Pitch.query.filter_by(id=check_pitch.user_id, name="Cool things and Cooler things").first()

    #     self.assertFalse(deleted_pitch)
    
if __name__ == "__main__":

    # Create database
    drop_database(env)
    create_database(env)
    add_dummy_data(env)

    # Run tests
    unittest.main()
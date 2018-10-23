import os
import unittest

from run import create_app
from database import db
from models.user import User
from db_create

app = create_app('TESTING')

class UserTests(unittest.TestCase):
    ''' User entity test suite '''

    def setUp(self):
        self.app = app.test_client()
        db.init_app(self.app)
        add_dummy_data

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_setup(self):
        new_user = User("Joey Smith", "joe@joe.com", "rofl1234")
        db.session.add(new_user)
        db.session.commit()
    

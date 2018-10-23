import os
import unittest

from run import create_app
from models.user import User

app = create_app('TESTING')

class UserTests(unittest.TestCase):
    ''' User entity test suite '''

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_setup(self):
        new_user = User("Joey Smith", "joe@joe.com", "rofl1234")
        db.session.add(new_user)
        db.session.commit()
    

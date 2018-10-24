import os
import unittest

from run import create_app
from database import db
from models.user import User
from db_create import create_database
from db_dummy import add_dummy_data

env = 'TESTING'


class UserTests(unittest.TestCase):
    ''' User entity test suite '''

    def setUp(self):
        self.app = create_app(env)
        self.client = self.app.test_client()
        create_database(env)
        add_dummy_data(env)
        db.init_app(self.app)
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_add(self):
        new_user = User("Joey Smith", "joe@joe.com", "rofl1234")
        db.session.add(new_user)
        db.session.commit()
        check_user = User.query.filter_by(id=new_user.id).first()

        assert check_user == new_user
    

if __name__ == "__main__":
    unittest.main()
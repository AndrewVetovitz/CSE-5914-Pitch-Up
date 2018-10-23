from sqlalchemy import Column, Integer, String
from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, name, email, password):
        ''' Create a new user '''

        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User(Id: '{}', Name: '{}', Email: '{}')>".format(self.id, self.name, self.email)

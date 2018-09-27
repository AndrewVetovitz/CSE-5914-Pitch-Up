from sqlalchemy import Column, Integer, String
from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(Id: '{}', Name: '{}', Email: '{}')>".format(self.id, self.name, self.email)

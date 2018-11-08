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

    def update(self, name, email, password):
        ''' Update user '''

        print("name={} email={} password={}".format(name, email, password))

        print(name == '')

        self.name = self.name if (name == None or name == '') else name
        self.email = self.email if (email == None or email == '') else email
        self.password = self.password if (password == None or password == '') else password
        
    @property
    def serialize(self):
        """ Return object data in easily serializeable format """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
    
    def __repr__(self):
        return "<{}(Id={}, Name={}, Email={})>".format(self.__class__.__name__, self.id, self.name, self.email)

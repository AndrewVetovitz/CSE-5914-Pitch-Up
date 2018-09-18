from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     email = Column(String)
     password = Column(String)

     def __repr__(self):
        return "<User(name='%s', fullname='%s', email='%s', password='%s')>" % (
            self.name, self.fullname, self.email, self.password)

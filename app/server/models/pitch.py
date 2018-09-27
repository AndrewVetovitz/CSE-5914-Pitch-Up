from sqlalchemy import Column, Integer, String, ForeignKey
from database import db

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    
    def __repr__(self):
        return "<Pitch(Id: '%s', Name: '%s')>" % (str(self.id), self.name)

from sqlalchemy import Column, Integer, String
from models import Base

class Pitch(Base):
    __tablename__ = 'pitches'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String)
    
    def __repr__(self):
        return "<Pitch(Id: '%s', Name: '%s')>" % (str(id), self.name)

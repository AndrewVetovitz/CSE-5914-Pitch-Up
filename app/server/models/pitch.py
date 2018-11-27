from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import db

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    query_concepts = Column(String)
    related_concepts = Column(String)
    top_entities = Column(String)

    # Will cascade delete all children
    children = relationship("PitchTry", cascade="all,delete", backref="Pitch")
    
    def __repr__(self):
        return "<{}(Id={}, Name={})>".format(self.__class__.__name__, str(self.id), self.name)

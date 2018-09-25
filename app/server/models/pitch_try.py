from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import db

class PitchTry(db.Model):
    __tablename__ = 'pitch_tries'

    id = Column(Integer, primary_key=True)
    pitch_id = Column(Integer, ForeignKey('pitches.id'))
    date = Column(DateTime)
    total_words = Column(Integer)
    
    
    def __repr__(self):
        return "<PitchTry(Id: '%s', PitchId: '%s')>" % (str(self.id), self.name)
    
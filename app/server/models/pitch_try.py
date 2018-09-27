from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from database import db

class PitchTry(db.Model):
    __tablename__ = 'pitch_tries'

    id = Column(Integer, primary_key=True)
    pitch_id = Column(Integer, ForeignKey('pitches.id'))
    date = Column(DateTime)
    is_analyzed = Column(Boolean, default = False)
    duration = Column(Integer)
    transcription = Column(String)
    
    def __repr__(self):
        return "<PitchTry(Id: '{}')>".format(str(self.id))
    
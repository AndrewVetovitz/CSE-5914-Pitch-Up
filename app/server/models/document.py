from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import db
from datetime import datetime

class Document(db.Model):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    pitch_id = Column(Integer, ForeignKey('pitches.id'))
    date = Column(DateTime)

    def __init__(self, name, pitch_id):
        self.pitch_id = pitch_id
        self.name = name
        self.date = datetime.now()

    def __repr__(self):
        return "<{}(Id={}, Name={}, PitchId={})>".format(self.__class__.__name__, str(self.id), self.name, self.pitch_id)

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from database import db

import re

WORDS_UMM = ''
WORDS_EXPLITIVES = ['shit', 'fuck', 'damnit', 'damn']

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
    
    def analyze(self):
        
        # Words
        num_explitives = 0
        for word in WORDS_EXPLITIVES:
            if word in self.transcription:
                num_explitives += 1

        num_stop_words = 0
        for word in WORDS_EXPLITIVES:
            if word in self.transcription:
                num_explitives += 1

        word_analysis = {
            'explitives': num_explitives,
            'stop_words': num_stop_words
        }






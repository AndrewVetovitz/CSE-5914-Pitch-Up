from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from database import db
import json
from datetime import datetime

from models.pitch import Pitch
from models.user import User

from helpers.analysis import Analysis

import re

WORDS_UMM = ''
WORDS_EXPLITIVES = ['shit', 'fuck', 'damnit', 'damn']
WORDS_STOP = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

class PitchTry(db.Model):
    __tablename__ = 'pitch_tries'

    id = Column(Integer, primary_key=True)
    pitch_id = Column(Integer, ForeignKey('pitches.id'))
    date = Column(DateTime)
    is_analyzed = Column(Boolean, default = False)
    duration = Column(Integer)
    words_per_minute = Column(Integer)
    transcription = Column(String)
    analysis_words = Column(String)
    analysis_concepts = Column(String)

    def __init__(self, pitch_id, transcription, duration):
        self.pitch_id = pitch_id
        self.transcription = transcription
        self.duration = duration
        self.date = datetime.now()
        self.is_analyzed = False
        self.analysis_words = ''

        analysis = Analysis()

        if transcription:
            self.words_per_minute = analysis.words_per_minute(transcription, duration)

            word_analysis = {
                'explitives': analysis.num_char_per_word(transcription, '*'),
                'stop_words': analysis.num_occurences(transcription, WORDS_STOP),
                'tone': analysis.tone_anaysis(transcription),
                'contains_name': analysis.contains_name(transcription, self.get_user_name)
            }

            self.analysis_words = json.dumps(word_analysis)
            
            pitch = Pitch.query.filter_by(id = self.pitch_id).first()
            self.analysis_concepts = analysis.discovery_analysis(transcription, pitch)
            
            self.is_analyzed = True

    @property
    def get_user_name(self):
        pitch = Pitch.query.filter_by(id = self.pitch_id).first()
        user = User.query.filter_by(id = pitch.user_id).first()
        return user.name

    @property
    def serialize(self):
        """ Return object data in easily serializeable format """
        return {
            'id': self.id,
            'is_analyzed': self.is_analyzed,
            'transcription': self.transcription,
            'analysis_words': json.loads(self.analysis_words),
            'analysis_concepts': self.analysis_concepts,
            'duration': self.duration,
            'words_per_minute': self.words_per_minute
        }

    def __repr__(self):
        return "<{}(Id={}, pitch_id={}, date={}, is_analyzed={}, duration={}, words_per_minute={}, transcription={}, analysis_words={}, analysis_concepts={})>".format(
            self.__class__.__name__, str(self.id), self.pitch_id, self.date, self.is_analyzed, self.duration, self.words_per_minute, self.transcription, self.analysis_words, self.analysis_concepts)

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from database import db
import json
from datetime import datetime

from models.pitch import Pitch

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
        self.analysis_concepts = ''

        # Analyze pitch try
        self.analyze()

    
    def __repr__(self):
        return "<PitchTry(Id: '{}', pitch_id: '{}', date: '{}', is_analyzed: '{}', duration: '{}', words_per_minute: '{}', transcription: '{}', analysis_words: '{}', analysis_concepts: '{}')>".format(
            str(self.id), self.pitch_id, self.date, self.is_analyzed, self.duration, self.words_per_minute, self.transcription, self.analysis_words, self.analysis_concepts)
    
    def analyze(self):
        trans_list = self.transcription.split()

        # Words per minute
        if self.duration == 0:
            self.words_per_minute = 0
        else:
            words_per_minute = float(len(trans_list) * 60) / float(self.duration)
            self.words_per_minute = round(words_per_minute, 2)

        # Words
        num_explitives = 0
        for word in WORDS_EXPLITIVES:
            if word in trans_list:
                num_explitives += 1

        num_stop_words = 0
        for word in WORDS_STOP:
            if word in trans_list:
                num_stop_words += 1

        num_umms = 0
        # for word in WORDS_EXPLITIVES:
        #     if word in self.transcription:
        #         num_explitives += 1

        word_analysis = {
            'explitives': num_explitives,
            'stop_words': num_stop_words
        }

        self.analysis_words = json.dumps(word_analysis)

        # Watson
        # Simple for now... Check if any words matched the concepts from Watson
        concept_analysis = {}
        pitch = Pitch.query.filter_by(id = self.pitch_id).first()
        print("got pitch:", pitch)
        print(pitch.related_concepts)
        if pitch.related_concepts:
            concepts = (" ".join(json.loads(pitch.related_concepts)).lower()).split()
            for word in trans_list:
                if word in concepts:
                    concept_analysis[word] = concept_analysis.get(word, 0) + 1
            
            self.analysis_concepts = json.dumps(concept_analysis)
            print(self.analysis_concepts)

        # Finally, set to analyzed and we're done.
        self.is_analyzed = True


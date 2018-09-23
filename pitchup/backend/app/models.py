from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from app.database import db


class User(db.Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(Id: {}, Name: {}, Email: {}')>".format(
                str(self.id), self.name, self.email
            )


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    
    def __repr__(self):
        return "<Pitch(Id: {}, Name: {})>".format(
            str(self.id), self.name
            )


class PitchTry(db.Model):

    __tablename__ = 'pitch_tries'

    id = Column(Integer, primary_key=True)
    pitch_id = Column(Integer, ForeignKey('pitches.id'))
    date = Column(DateTime)
    total_words = Column(Integer)
    
    
    def __repr__(self):
        return "<PitchTry(Id: {}, PitchId: {})>".format(
            str(self.id), self.name
            )



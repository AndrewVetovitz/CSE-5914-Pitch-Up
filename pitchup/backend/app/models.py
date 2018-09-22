from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import db

class User(db.Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', email='%s', password='%s')>" % (
                self.name, self.fullname, self.email, self.password
            )


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    
    def __repr__(self):
        return "<Pitch(Id: '%s', Name: '%s')>" % (str(id), self.name)

from sqlalchemy import Column, Integer, Date, ForeignKey
from database import db

class Report(db.Model):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    @property
    def serialize(self):
        """ Return object data in easily serializeable format """
        return {
            'id': self.id,
            'date': self.date,
            'user_id': self.user_id
        }

    def __repr__(self):
        return "<{}(date={}, user_id={})>".format(self.__class__.__name__, self.date, self.parent_id)

from sqlalchemy import Column, Integer, Date, ForeignKey
from database import db

class Report(db.Model):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "<Report(date='%s', user_id='%s')>" % (
                self.date, self.parent_id
            )

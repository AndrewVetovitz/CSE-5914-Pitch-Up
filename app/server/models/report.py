from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "<Report(date='%s', user_id='%s')>" % (
                self.date, self.parent_id
            )

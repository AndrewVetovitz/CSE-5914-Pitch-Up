from sqlalchemy import Column, Integer, String
from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    company = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postal = Column(String)
    bio = Column(String)

    def __init__(self, name, username, email, password, company=None, city=None, state=None, country=None, postal=None, bio=None):
        ''' Create a new user '''

        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.company = company or ''
        self.city = city or ''
        self.state = state or ''
        self.country = country or ''
        self.postal = postal or ''
        self.bio = bio or ''

    def update(self, name, username, email, password, company, city, state, country, postal, bio):
        ''' Update user '''

        self.name = self.name if (name == None or name == '') else name
        self.username = self.username if (username == None or username == '') else username
        self.email = self.email if (email == None or email == '') else email
        self.password = self.password if (password == None or password == '') else password
        self.company = self.company if (company == None or company == '') else company
        self.city = self.city if (city == None or city == '') else city
        self.state = self.state if (state == None or state == '') else state
        self.country = self.country if (country == None or country == '') else country
        self.postal = self.postal if (postal == None or postal == '') else postal
        self.bio = self.bio if (bio == None or bio == '') else bio
        
    @property
    def serialize(self):
        """ Return object data in easily serializeable format """
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'company': self.company,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'postal': self.postal,
            'bio': self.bio
        }
    
    def __repr__(self):
        return "<{}(Id={}, Name={}, Username={}, Email={}, Password={}, Company={}, City={}, State={}, Country={}, Postal={}, Bio={})>".format(
            self.__class__.__name__, self.id, self.name, self.username, self.email, self.password, self.company, self.city, self.state, self.country, self.postal, self.bio)

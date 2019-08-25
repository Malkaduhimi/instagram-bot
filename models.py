from sqlalchemy import Column, String, Integer, Date, Text
from base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    user_id = Column(Integer)
    follow_date = Column(Date)
    unfollow_date = Column(Date)

    def __init__(self, user_id, username, follow_date, unfollow_date=None):
        self.user_id = user_id
        self.username = username
        self.follow_date = follow_date
        self.unfollow_date = unfollow_date

class Account(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    user_id = Column(Integer)
    login_date = Column(Date)
    instagram_object = Column(Text)

    def __init__(self, user_id, username, login_date, instagram_object):
        self.user_id = user_id
        self.username = username
        self.login_date = login_date
        self.instagram_object = instagram_object

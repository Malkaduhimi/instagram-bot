from sqlalchemy import Column, String, Integer, Date
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

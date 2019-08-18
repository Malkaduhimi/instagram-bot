from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data/db.sqlite')
Session = sessionmaker(bind=engine)
connection = engine.connect()
Base = declarative_base()


import os
import json
from datetime import datetime
from sqlalchemy import ForeignKey, desc, create_engine, func, Column, BigInteger, Integer, Float, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pprint import pprint

engine = create_engine(os.environ.get('TWENDS_DATABASE'), echo=False)
Base = declarative_base()

class Location(Base):
  __tablename__ = 'location'

  Id = Column('id', Integer, primary_key=True)
  Value = Column('value', Text)

  def __init__(self, data):
    self.Id = data['id']
    self.Value = data['value']

class Run(Base):
  __tablename__ = 'run'

  Id = Column('id', Integer, primary_key=True)
  Location = Column('location', Integer, ForeignKey('location.id'))
  Time = Column('time', DateTime)

  def __init__(self, data):
    self.Location = data['location']
    self.Time = data['time']

class Trend(Base):
  __tablename__ = 'trend'

  Id = Column('id', Integer, primary_key=True)
  Value = Column('value', Text)
  Place = Column('place', Integer)
  Volume = Column('volume', Integer)
  Run = Column('run', Integer, ForeignKey('run.id'))

  def __init__(self, data):
    self.Value = data['value']
    self.Volume = data['volume']
    self.Place = data['place']
    self.Run = data['run']

class Operations:
  def SaveRun(data):
    run = Run(data)
    session.add(run)
    session.flush()

    for trend in data['trends']:
      trend['run'] = run.Id
      session.add(Trend(trend))

    session.commit()

  def QueryLocation():
    return session.query(Location).all()

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

if __name__ == "__main__":
  pprint(Operations.QueryLocation()[0].__dict__)

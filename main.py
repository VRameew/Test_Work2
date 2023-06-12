import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI

#Data class for SQL base
Base = declarative_base()


class Users(Base):


class Records(Base):

#Creating SQL Base
engine = sa.create_engine("postgresql+psycopg2://postgres:postgres@DB", echo=True, pool_pre_ping=True)
#Creating tables
Base.metadata.create_all(engine)

DBSession = sessionmaker(
    binds={Base: engine},
    expire_on_commit=False,
)
session = DBSession()

#Start FastAPI APP
app = FastAPI()

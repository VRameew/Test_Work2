import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI, HTTPException
import uuid

#Data class for SQL base
Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Text, nullable=False)
    token = sa.Column(sa.Text, nullable=False)


class Record(Base):
    __tablename__ = "Records"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Text, nullable=False)
    url = sa.Column(sa.Text, nullable=False)

#Creating SQL Base
engine = sa.create_engine("postgresql+psycopg2://postgres:postgres@localhost/DB", echo=True, pool_pre_ping=True)
#Creating tables
Base.metadata.create_all(engine)

DBSession = sessionmaker(
    binds={Base: engine},
    expire_on_commit=False,
)
session = DBSession()

#Start FastAPI APP
app = FastAPI()
#Finding users by token
def get_user(token: str):
    users = session.query(User).all()
    for user in users:
        if user.token == token:
            return user
    raise HTTPException(status_code=401, detail="Invalid token")
    
@app.post("/users", response_model=User)
def user_creating("/users", response_model=User):
    id = str(uuid.uuid4())
    token = str(uuid.uuid4())
    user = User(id=id, name=name, token=token)
    session.add(user)
    session.commit()
    return user

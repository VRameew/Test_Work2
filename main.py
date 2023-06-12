import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI, HTTPException, File
from fastapi.responses import FileResponse
import uuid
import os, subprocess
import time

# Data class for SQL base
Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.Text, nullable=False)
    token = sa.Column(sa.Text, nullable=False)


class Records(Base):
    __tablename__ = "Records"
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column(sa.Integer, nullable=False)
    uuid_file = sa.Column(sa.Text, nullable=False)

# Creating SQL Base
engine = sa.create_engine("postgresql+psycopg2://postgres:postgres@DB", echo=True, pool_pre_ping=True)
# Creating tables
Base.metadata.create_all(engine)
DBSession = sessionmaker(
    binds={Base: engine},
    expire_on_commit=False,
)
session = DBSession()
# Start FastAPI APP
app = FastAPI()
# Finding users and records by token
def get_user(token: str):
    users = session.query(Users).all()
    for user in users:
        if user.token == token:
            return user
    raise HTTPException(status_code=401, detail="Invalid token")
    
def get_record(uuid_file: str):
    records = session.query(Records).all()
    for rec in records:
        if rec.uuid_file == uuid_file:
            return rec
    raise HTTPException(status_code=401, detail="Invalid token")


# First part of API
@app.post("/users")
def user_creating(name: str):
    token = str(uuid.uuid4())
    user = Users(name=name, token=token)
    session.add(user)
    session.commit()
    return [user.id, user.token]

# Second part API. Takes  paramas user_id, token and data(file for upload)  
@app.post("/records")
def add_record(user_id: int, token: str, data: bytes = File()):
    user = get_user(token)
    if user.id != user_id:
        raise HTTPException(status_code=401, detail="User ID mismatch")
    
    uuid_file = str(uuid.uuid4())
    record_path = f"{uuid_file}.wav"
    mp3_path = f"{uuid_file}.mp3"
    with open(record_path, "wb") as f:
        f.write(data)
    subprocess.run(["ffmpeg.exe", "-i", record_path, "-f", "mp3", mp3_path])
    record = Records(user_id=user_id, uuid_file=uuid_file)
    session.add(record)
    session.commit()
    record = get_record(uuid_file)
    return (f"http://localhost:8000/record?id={record.id}&user={user_id}")

# Third part of API takes id of record and user id for donload link generate     
@app.get("/record")
def get_records(id: int, user: int):
    record = None
    records = session.query(Records).all()
    for rec in records:
        if rec.id == id and rec.user_id == user:
            record = rec
            break
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")

    return FileResponse(f"{record.uuid_file}.mp3")


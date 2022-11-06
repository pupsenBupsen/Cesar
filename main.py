from fastapi import FastAPI
from pydantic import BaseModel
from database import Base, engine, Rot
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)    

class Body(BaseModel):
    message: str
    rot: int 

app = FastAPI()
alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar (message:str, rot:int):
    caesar_message = ''
    for i in message:
        caesar_message += alfavit[alfavit.find(i.upper())+rot]
        print(i)
    return caesar_message
    
@app.post("/encode")
async def root(item: Body):
    x = caesar(item.message, item.rot)
    session = Session(bind=engine, expire_on_commit=False)
    rotdb = Rot(count = 1, rot = item.rot)
    session.add(rotdb)
    session.commit()
    id = rotdb.rot
    session.close()

    return {"message": x, "id": id}

@app.get("/encode/decode")
async def decode(message:str, rot:int):
    return{"message": caesar(message, -rot)}

@app.get("/stats")
async def stats():
    return ["rot", "usages"]
from fastapi import FastAPI 
from pydantic import BaseModel

app=FastAPI() 

class Student(BaseModel):
    name: str
    rollno: int
    city: str 

@app.post("/") #get and post you can use
async def show(s1:Student):
    return s1    
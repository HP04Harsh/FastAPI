from fastapi import *

app = FastAPI() 

@app.post("/")
async def push(name: str = Body(...)):
  return {"name":name}
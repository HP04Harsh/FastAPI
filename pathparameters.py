from fastapi import FastAPI 

app = FastAPI() 

@app.get("/users/{name}") #Path Parameter
async def show(name: str):
    return {"Name":name}
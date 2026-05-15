from fastapi import FastAPI, Depends

app = FastAPI()

def users(id: int, name: str):
    return {"id":id, "name": name}

@app.get("/")
async def show(user: dict = Depends(users)):
    return user    
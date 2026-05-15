from fastapi import FastAPI , Path, Query

app = FastAPI() 

@app.get("/users/{name}")
async def show(name: str=Path(...,min_length=5,max_length=10),age:int=Query(None,min_length=2)): 
    return {"Name":name,"Age":age}
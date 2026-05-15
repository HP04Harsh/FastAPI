from fastapi import FastAPI 
from fastapi.responses import HTMLResponse 

app = FastAPI() 

@app.get("/users/{name}")
async def show(name: str):
    content = f'''
      <html>
      <body>
        <h2> {name} </h2>
      </body>
      </html>
    '''
    return HTMLResponse(content=content)    
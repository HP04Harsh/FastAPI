from fastapi import *
from fastapi.templating import * 
from fastapi.responses import *

app = FastAPI() 

templates = Jinja2Templates("templates")

@app.get("/user/{name}",response_class=HTMLResponse)
async def show(request:Request,name: str):
    return templates.TemplateResponse(
        request = request,
        name = "index.html",
        context = {
            "name": name
        }
    )

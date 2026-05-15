# CMD - pip install aiofiles

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI() 

app.mount("/static",StaticFiles(directory="templates"),name="static")
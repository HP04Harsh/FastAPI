from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def set_rsp_headers():
   content = {"message": "Hello World"}
   headers = {"X-Web-Framework": "FastAPI", "Content-Language": "en-US"}
   return JSONResponse(content=content, headers=headers)
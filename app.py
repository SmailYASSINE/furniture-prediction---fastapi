from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import pickle
from jinja2 import Environment, FileSystemLoader
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from typing import Annotated

# Bring in lightweight dependencies
from fastapi import FastAPI,  Request, Form
import pickle
#import preprocess as ps 
import pandas as pd
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

with open('model.pkl', 'rb') as f: 
    model = pickle.load(f)
 



app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/" )

def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})
@app.post('/predict')

async def predict( request: Request, category: Annotated[float, Form()],sellable_online: Annotated[float, Form()],other_colors: Annotated[float, Form()],depth: Annotated[float, Form()],height: Annotated[float, Form()],width: Annotated[float, Form()] ):
    try:
        prediction = model.predict([[category, sellable_online, other_colors, depth, height, width]])[0]
        return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "prediction": f"Error: {str(e)}"})



if __name__ == '__main__':
    uvicorn.run(app)
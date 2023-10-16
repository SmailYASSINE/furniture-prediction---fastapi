from fastapi import FastAPI, Request
import uvicorn
import pickle
from fastapi.templating import Jinja2Templates
import numpy as np
# Bring in lightweight dependencies
from fastapi import FastAPI,  Request, Form
import pickle
import pandas as pd
from fastapi.templating import Jinja2Templates
import uvicorn
model = pickle.load(open('C:\\Users\\um6p\\Desktop\\M1\\M2\\kelloubi\\Lab folder - FastAPI Pydantic\\FastApi - previous assignment\\model.pkl', 'rb'))


app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# list of one-hot encoded airline options
airline_options = {
    'Air India': [1, 0, 0, 0, 0],
    'GO FIRST': [0, 1, 0, 0, 0],
    'Indigo': [0, 0, 1, 0, 0],
    'SpiceJet': [0, 0, 0, 1, 0],
    'Vistara': [0, 0, 0, 0, 1]
}

# list of one-hot encoded flight options
flight_options = {
    'UK-720': [1, 0, 0, 0, 0],
    'UK-822': [0, 1, 0, 0, 0],
    'UK-826': [0, 0, 1, 0, 0],
    'UK-828': [0, 0, 0, 1, 0],
    'UK-874': [0, 0, 0, 0, 1]
}

@app.route('/')
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.route('/predict')
async def predict(
    request: Request,
    stops: float = Form(...),
    _class: float = Form(...),
    duration: float = Form(...),
    days_left: float = Form(...),
    airline: str = Form(...), 
    flight: str = Form(...),
    arrival_time: float = Form(...),
    departure_time: float = Form(...)
):
    
    try:
        # I handle one-hot encoded airline variable
        selected_airline = airline_options.get(airline, [0, 0, 0, 0, 0])
        
        # I handle one-hot encoded flight variable
        selected_flight = flight_options.get(flight, [0, 0, 0, 0, 0])

        final_features = [
            stops,
            _class,
            duration,
            days_left
        ]

        final_features.extend(selected_airline)
        final_features.extend(selected_flight)
        final_features.append(arrival_time)
        final_features.append(departure_time)

        # Reshape the features to match the model's input shape (1, num_features)
        final_features = np.array(final_features).reshape(1, -1)

        prediction = model.predict([final_features])  
        output = round(prediction[0], 2)

        # Return the prediction to be displayed on the HTML page
        return templates.TemplateResponse("index.html", {"request": request, "prediction_text": output})
    
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "prediction_text": f"Error: {str(e)}"})

if __name__ == '__main__':
    uvicorn.run(app)
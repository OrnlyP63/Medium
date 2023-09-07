from fastapi import FastAPI
from pydantic import BaseModel, conlist
from typing import List
from joblib import load

# the type of input data
class WineQuality(BaseModel):
    data: List[conlist(float, min_items=11, max_items=11)]

# an instance of app
app = FastAPI(title="Wine Quality ML API", description="API for wine-qualities ml model", version="1.0")

# initialize the model
@app.on_event("startup")
def load_model():
    app.model, app.columns = load('models/svc.joblib') # assigned the loaded model to app.model

# a prediction model
@app.post("/predict")
async def predict(user_input:WineQuality):
    data = dict(user_input)['data']
    result = app.model.predict(data)
    return result.item() # remark: could return dict or numerical type, not return others (such as np.ndarray)
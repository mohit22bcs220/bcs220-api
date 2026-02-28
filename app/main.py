from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    try:
        prediction = (
            data.feature1 +
            data.feature2 +
            data.feature3 +
            data.feature4
        )
        return {"prediction": prediction}
    except:
        raise HTTPException(status_code=400, detail="Invalid input")
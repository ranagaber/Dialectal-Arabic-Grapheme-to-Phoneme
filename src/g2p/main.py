from fastapi import FastAPI
from g2p.app import get_phoneme
from pydantic import BaseModel

app = FastAPI()


class Request(BaseModel):
    country_id: str
    text: str

class Response(BaseModel):
    prediction: str

@app.get("/")
def root():
    return {"message": "API is running"}


@app.post("/get_phoneme", response_model=Response)
def predict_endpoint(request: Request):
    text = "[" + request.country_id + "]" + request.text
    pred = get_phoneme(text)

    return {"prediction": pred}
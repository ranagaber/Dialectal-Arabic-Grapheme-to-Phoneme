from fastapi import FastAPI
from g2p.app import get_phoneme
from pydantic import BaseModel
app = FastAPI()

class Request(BaseModel):
    text: str

class Response(BaseModel):
    text: str

@app.get("/")
def root():
    return {'message' : "API is running"}
@app.post("/get_phoneme" , response_model=Response)
def predict_endpoint(request:Request):
    pred = get_phoneme(request.text)

    return {"prediction" : pred}
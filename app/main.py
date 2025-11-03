from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Kubernetes POC running successfully"}

@app.get("/predict")
def predict(value: int):
    return {"input": value, "prediction": value * 2}

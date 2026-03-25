from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI CD Workinggg 🚀"}

@app.get("/yuvraj")
def home():
    return {"message": "Hey Yuvraj 🚀"}
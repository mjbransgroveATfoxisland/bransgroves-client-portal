from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Test API is working!"}
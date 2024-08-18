from fastapi import FastAPI

from api import api

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fast API in Python"}

@app.get("/users")
def get_users():
    return api.read_user()
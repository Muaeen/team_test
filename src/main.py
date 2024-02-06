import numpy as np 
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def main():
    return {"hi"}

@app.get("/")
def cak():
    return 1 + 2
# print(main())
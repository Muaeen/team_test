import numpy as np 
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def main():
    return {"hi"}

# print(main())
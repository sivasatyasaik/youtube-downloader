
from typing import Dict, Union
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allow all origins (use a list of origins in production)
    allow_credentials=True,
    allow_methods=["*"],      # Allow all HTTP methods
    allow_headers=["*"],      # Allow all headers
)

@app.post("/add")
def add_num(a: int = Form(...), b: int = Form(...)):
    return {"sum": a + b}

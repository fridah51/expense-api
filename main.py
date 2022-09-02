from fastapi import FastAPI
from datetime import datetime
from typing import Dict, Generator, List
from fastapi.middleware.cors import CORSMiddleware


#router
from api_routes.api import router

app = FastAPI(
    title="Expenses API",
    description = "A basic expenses api",
    version = "0.1.0",
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, responses={200:{"description":"Ok"}})


@app.get("/", 
summary="Home route",
status_code=200,
)
def home():
    
   return "Hey you ..."



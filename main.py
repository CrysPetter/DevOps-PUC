import random
from typing import Union

from fastapi import FastAPI

app = FastAPI()

# acesso http://127.0.0.1:8000
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# acesso http://127.0.0.1:8000/item1
@app.get("funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint( a: 0, b: 100)}
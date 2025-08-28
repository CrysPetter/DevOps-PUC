from typing import Union

from fastapi import FastAPI

app = FastAPI()

# acesso http://127.0.0.1:8000
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# acesso http://127.0.0.1:8000/item1
@app.get("/item1")
async def read_item():
    return {"item1": "Deu Certo"}
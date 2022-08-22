from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import json

import requests

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    url = 'https://62f6640ba3bce3eed7c04b72.mockapi.io/items'
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json() }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/{item_id}")###################
def upload_item(item_id: int, item: Item):
    #url = 'https://62f6640ba3bce3eed7c04b72.mockapi.io/items'
    #obj = {'item_name': item.name}
    #requests.post(url, json= obj)
    return {"item_name": item.name, "item_id": item_id}

@app.delete("/items/")########################
def delete_item():
    url = 'https://62f6640ba3bce3eed7c04b72.mockapi.io/items'
    response = requests.delete(url)
    return {"items": response.json() }

























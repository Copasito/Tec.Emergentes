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

header = {'Content-type': 'application/json', 'Accept': 'Application/json'}
url = 'https://62f6640ba3bce3eed7c04b72.mockapi.io/items'
#url = 'https://6303e5400de3cd918b3fde59.mockapi.io/items' getitem put post
@app.get("/")
def read_root():   
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json() }

@app.get("/items/{item_id}")
def read_item(item_id: int):
    response = requests.get(url+'/'+str(item_id), timeout=5)
    return {"item": response.json()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    requests.put(url+"/"+str(item_id), item.json(), headers=header)
    return "Se añadio el nuevo producto"

@app.post("/items/{item_id}")
def upload_item(item_id: int, item: Item):
    requests.post(url, item.json(), headers=header)
    return "Se añadio el nuevo producto"

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    response = requests.delete(url+"/"+str(item_id))
    return {"items": response.json() }


























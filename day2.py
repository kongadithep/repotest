from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel


class Item(BaseModel):
    item_id:int = 0,
    item_name: str = " "
    item_bool: Union[bool,None] = False


app = FastAPI()

@app.get("/")
def root():
    return {"msg":"Love mom "}

@app.get("/items/{item_id}/{item_name}/{item_bool}")
def show_item(item_id:int, item_name :str , item_bool :bool):
    return {"item_id": item_id, "item_name":item_name,"item_bool":item_bool}

@app.post("/items", status_code=201)
def create_item():
    return {"msg": "created"}


@app.get("/items")
def quert_item(item_id:int, item_name :str , item_bool :bool):
    return {"item_id": item_id, "item_name":item_name,"item_bool":item_bool}


@app.get("/items")
def show_item_body(item: Item):
    return {"item" : item}

@app.get("/items/combine/{item_id}")
def combine_all_params(item_id:str,item_name:str,item_detail:Item):
    return {"item_id":item_id,"item_name":item_name,"item_detail":item_detail}
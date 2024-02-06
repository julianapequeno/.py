from fastapi import FastAPI
# trabalha com funções que recebem apenas um argumento de algum tipo de um leque de opções deles
from typing import Union
from pydantic import BaseModel

app = FastAPI()  # elemento que recebe da lib do fastapi


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def root():
    return {"mensagem": "Olá, Womakers!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, busca: Union[str, int] = None):
    return {"item_id": item_id, "busca": busca}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item.id}

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


class Report(BaseModel):
    reportId: int


@app.get("/")
async def create_item():
    return {"message": "hello"}


@app.post("/items/")
async def create_item(item: Item):
    # 받은 아이템을 처리하는 로직을 구현합니다.
    # 여기서는 간단히 아이템 정보를 반환합니다.
    return {"message": "Item created", "item": item}


@app.post("/load/report")
async def create_item(report: Report):
    return {"message": "load report", "report": report}

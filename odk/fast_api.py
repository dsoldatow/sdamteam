import http
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://0.0.0.0:8080",
    "https://sdamteam.herokuapp.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ActionVk(BaseModel):
    type: str
    object: dict
    group_id: int


@app.post("/vk_bot")
def read_root(action: ActionVk):
    print(action)
    return http.HTTPStatus.OK


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


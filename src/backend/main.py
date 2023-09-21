from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class LoginClass(BaseModel):
    username: str
    password: str

@app.get("/)
        


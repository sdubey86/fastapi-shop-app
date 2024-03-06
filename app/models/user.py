from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    orders: List[int] = []
from pydantic import BaseModel

class ProductBase(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    quantity: int

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int

class ProductUpdate(ProductBase):
    id: int
    name: str
    description: str | None = None
    price: float
    quantity: int

class Product(ProductBase):
    pass

    class Config:
        orm_mode = True
from pydantic import BaseModel

class ProductBase(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    pass

    class Config:
        orm_mode = True
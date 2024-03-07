from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.products import Product
from app.schemas.products import ProductUpdate, ProductBase, ProductCreate
from app.db.database import get_db 

productRouter = APIRouter(
    prefix="/products",
    tags=["products"]
)

@productRouter.post("/", response_model=ProductBase)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return Product.create(db, product=product)

@productRouter.get("/", response_model=list[ProductBase])
async def get_products(db: Session = Depends(get_db)):
    return Product.get_all(db)

@productRouter.get("/{product_id}", response_model=ProductBase)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = await Product.get(db, product_id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product
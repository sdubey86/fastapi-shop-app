from sqlalchemy import Integer, String, Float, Column, Text
from sqlalchemy.orm import Session

from app.db.database import Base, engine
from app.schemas import Product, ProductCreate, ProductUpdate

# Ensure tables are created (run once or integrate into a migration system)
Base.metadata.create_all(bind=engine)

# CRUD Operations
async def create_product(db: Session, product: ProductCreate) -> Product:
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

async def get_product(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()

async def get_products(db: Session) -> list[Product]:
    return db.query(Product).all()

async def update_product(db: Session, product_id: int, product: ProductUpdate) -> Product:
    db_product = await get_product(db, product_id)
    if db_product:
        update_data = product.dict(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_product, key, value)

        db.commit()
        db.refresh(db_product)
        return db_product
    else:
        return None

async def delete_product(db: Session, product_id: int) -> None:
    db_product = await get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return None

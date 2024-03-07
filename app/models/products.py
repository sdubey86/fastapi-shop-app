from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from app.db.database import Base, engine
import sqlalchemy

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)
    quantity = Column(Integer) 


    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def create(cls, db: Session, product: 'ProductCreate') -> 'Product':
        db_product = cls(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product.__dict__

    @classmethod
    def get(cls, db: Session, product_id: int) -> 'Product':
        return db.query(cls).filter(cls.id == product_id).first().__dict__
    

    @classmethod
    def get_all(cls, db: Session) -> list['Product']:
        return [product.to_dict() for product in db.query(cls).all()]
    
    def get_total_quantity(cls, db: Session) -> int:
        return db.query(func.sum(cls.quantity)).scalar()

    @classmethod
    def update(cls, db: Session, product_id: int, product: 'ProductUpdate') -> 'Product':
        db_product = cls.get(db, product_id)
        if db_product:
            update_data = product.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_product, key, value)
            db.commit()
            db.refresh(db_product)
        return db_product
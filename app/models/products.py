from sqlalchemy import Integer, String, Float, Column, Text 
from app.db.database import Base  # Import the Base class

# Product SQLAlchemy Model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)


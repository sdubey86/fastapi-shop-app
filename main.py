from fastapi import FastAPI
from app.routes import hello_world, user, products
from sqlalchemy.orm import Session
from app.db.database import Base, engine

app = FastAPI()
app.include_router(hello_world.router) # This line is added to the main.py file
app.include_router(user.user_router)
app.include_router(products.productRouter)

@app.on_event("startup")
async def startup_event():
    create_tables()



def create_tables():
    with Session(engine) as session:
        Base.metadata.create_all(engine)

from fastapi import FastAPI
from app.routes import hello_world, user

app = FastAPI()
app.include_router(hello_world.router) # This line is added to the main.py file
app.include_router(user.user_router)

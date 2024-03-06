from fastapi import APIRouter, HTTPException
from app.mock.mock import mock_users
from app.models.user import User
user_router = APIRouter()

@user_router.get("/users/")
async def list_users():
    return mock_users


@user_router.get("/users/{user_id}")
async def user(user_id: int):
    return mock_users[user_id - 1]

@user_router.post("/users/", response_model=User, summary="Create a new user", description="Create a new user")
async def create_user(user: User):
    mock_users.append(user)
    return user

@user_router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for index, existing_user in enumerate(mock_users):
        if existing_user["id"] == user_id:
            mock_users.pop(index)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")


@user_router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for index, existing_user in enumerate(mock_users):
        if existing_user["id"] == user_id:
            updated_user = {"id": user_id, **user.dict()},
            mock_users[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")
from fastapi import APIRouter, HTTPException
from src.services.userService import UserService
from src.schemas.userSchema import UserCreate, UserUpdate, UserResponse

router = APIRouter()
service = UserService()

@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    return await service.create_user(user)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/", response_model=list[UserResponse])
async def get_all_users():
    return await service.get_all_users()

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user: UserUpdate):
    try:
        return await service.update_user(user_id, user)
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}", response_model=UserResponse)
async def delete_user(user_id: str):
    try:
        return await service.delete_user(user_id)
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")
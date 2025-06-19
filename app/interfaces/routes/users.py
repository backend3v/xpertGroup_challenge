from fastapi import APIRouter
from domain.services.users import create_user,get_all_users




router = APIRouter()




@router.get("/users")
async def get_users():
    users = get_all_users()
    return {"users": users}


@router.post("/init_user")
async def init_user(username: str, role: str):
    user = create_user(username, role)
    return {"message": "Usuario creado", "user_id": user.id}
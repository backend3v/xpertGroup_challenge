from fastapi import APIRouter
from domain.services.users import create_user,get_all_users
from domain.models.users import UserRequest





router = APIRouter()




@router.get("/users")
async def get_users():
    users = get_all_users()
    return {"users": users}


@router.post("/init_user")
async def init_user(user: UserRequest):
    user = create_user(user.username, user.role)
    return {"Id": user.id,"Name":user.username,"Role":user.role}
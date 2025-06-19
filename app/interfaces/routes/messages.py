from fastapi import APIRouter
from sqlmodel import Session
from domain.models.messages import Message
from adapters.database import engine


router = APIRouter()


@router.get("/history/{username}")
async def get_history(username: str):
    with Session(engine) as session:
        messages = session.query(Message).filter(Message.username == username).all()
        return messages
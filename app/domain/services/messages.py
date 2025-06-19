from sqlmodel import Session
from domain.models.messages import Message
from adapters.database import engine

def save_message(username: str, question: str, response: str):
    with Session(engine) as session:
        message = Message(username=username, question=question, response=response)
        session.add(message)
        session.commit()


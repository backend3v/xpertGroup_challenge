from sqlmodel import SQLModel, Field
from typing import Optional


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    question: str
    response: str
from sqlmodel import SQLModel, Field
from pydantic import BaseModel



class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True,index=True)
    username: str = Field(nullable=False)
    role: str = Field(nullable=False)

class UserRequest(BaseModel):
    username: str
    role: str
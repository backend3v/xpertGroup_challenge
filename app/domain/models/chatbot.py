from pydantic import BaseModel


class ChatbotRequest(BaseModel):
    username: str
    message: str
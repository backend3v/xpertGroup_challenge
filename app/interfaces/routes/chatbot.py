from fastapi import APIRouter
from domain.services.users import get_role
from domain.services.chatbot import get_chatbot_response
from domain.services.messages import save_message
from domain.models.chatbot import ChatbotRequest







router = APIRouter()




@router.post("/ask")
async def ask_chatbot(chatbot: ChatbotRequest):
    user_role = get_role(chatbot.username)
    if user_role is None:
        return {"response": "User not found"}
    response_chatbot = await get_chatbot_response(chatbot.message, user_role)
    response = response_chatbot.content
    save_message(chatbot.username, chatbot.message, response)
    return {"response": response}
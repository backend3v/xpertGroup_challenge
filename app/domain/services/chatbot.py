from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from config import settings
from fastapi import HTTPException


async def get_chatbot_response(question: str, role: str) -> str:
    try:
        chat_model = ChatOpenAI(model=settings.OPENAI_MODEL, openai_api_key=settings.OPENAI_API_KEY)
        prompt_template = PromptTemplate(
            input_variables=["role", "question"],
            template="Eres un {role}. Responde a la siguiente pregunta: {question}"
        )
        chain = prompt_template | chat_model
        response = chain.invoke({"role": role, "question": question})
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
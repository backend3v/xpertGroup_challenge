from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from config import settings


async def get_chatbot_response(question: str, role: str) -> str:
    chat_model = ChatOpenAI(model=settings.OPENAI_MODEL, openai_api_key=settings.OPENAI_API_KEY)
    prompt_template = PromptTemplate(
        input_variables=["role", "question"],
        template=f"""
        Eres un {role}. Debes proporcionar respuestas detalladas y precisas basadas en tu experiencia y conocimiento en este campo,
        para responder la siguiente pregunta:  "{question}".
        Responde de manera clara y profesional, asegurándote de abordar todos los aspectos relevantes del tema.
        """
    )
    chain = prompt_template | chat_model
    response = chain.invoke({"role": role, "question": question})
    return response
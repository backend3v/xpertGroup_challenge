import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))
    DATABASE_URL = os.getenv("DATABASE_URL")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL=os.getenv("OPENAI_MODEL")


settings = Settings()
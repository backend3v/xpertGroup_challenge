import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./challenge_xg.db")


settings = Settings()
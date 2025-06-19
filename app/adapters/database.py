from sqlmodel import SQLModel, create_engine
from config import settings




DATABASE_URL = settings.DATABASE_URL

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL no puede ser None")

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)

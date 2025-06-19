from sqlmodel import Session
from domain.models.users import User
from adapters.database import engine



def create_user(username: str, role: str):
    with Session(engine) as session:
        user = User(username=username, role=role)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
def get_all_users():
    with Session(engine) as session:
        users = session.query(User).all()
        return users
from fastapi import FastAPI
import uvicorn
from config import settings
from adapters.database import init_db
from interfaces.routes import users,chatbot


class Application:
    
    def __init__(self):
        self.app = FastAPI()
        self.configure()
    
    def configure(self):
        init_db()
        self.load_routes()
        
    def load_routes(self):
        self.app.include_router(users.router)
        self.app.include_router(chatbot.router)
        @self.app.get("/")
        async def root():
            return {"message": "Bienvenido a la API del chatbot"}
    
    def run(self):
        uvicorn.run(self.app, host=settings.HOST, port=settings.PORT)
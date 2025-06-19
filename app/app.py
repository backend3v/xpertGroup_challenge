from fastapi import FastAPI
import uvicorn
from config import settings
from adapters.database import init_db
from interfaces.routes import users,chatbot,messages
from interfaces.middlewares.api import ErrorHandlingMiddleware

class Application:
    
    def __init__(self):
        self.app = FastAPI()
        self.configure()
    
    def configure(self):
        init_db()
        self.app.add_middleware(ErrorHandlingMiddleware)
        self.load_routes()
        
    def load_routes(self):
        self.app.include_router(users.router)
        self.app.include_router(messages.router)
        self.app.include_router(chatbot.router)
        
    
    def run(self):
        uvicorn.run(self.app, host=settings.HOST, port=settings.PORT)
from fastapi import FastAPI
import uvicorn
from config import settings


class Application:
    
    def __init__(self):
        self.app = FastAPI()
        self.configure()
    
    
    def configure(self):
        self.load_routes()
        
    def load_routes(self):
        @self.app.get("/")
        async def root():
            return {"message": "Bienvenido a la API del chatbot"}
    
    
    def run(self):
        uvicorn.run(self.app, host=settings.HOST, port=settings.PORT)
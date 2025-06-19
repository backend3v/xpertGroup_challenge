from fastapi import APIRouter


router = APIRouter()



@router.get("/")
async def root():
    return {"message": "Bienvenido a la API del chatbot"}

@router.get("/health")
async def health_check():
    return {"status": "Healthy"}
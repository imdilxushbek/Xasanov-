from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def home():
    return {"message": "Xush kelibsiz, bu Xasanov Shop API"}
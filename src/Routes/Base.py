from fastapi import APIRouter
from src.Helpers.config import get_settings


router = APIRouter(prefix="/api/v1", tags=["Base"])

settings = get_settings()


@router.get("/Welcome")
async def WelcomeMessage():
    return f"Welcome to {settings.APP_NAME} v{settings.APP_VERSION}"

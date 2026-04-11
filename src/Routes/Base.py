from fastapi import APIRouter, Depends
from src.Helpers.config import get_settings, Settings

# DI for settings Depends()




router = APIRouter(prefix="/api/v1", tags=["Base"])


@router.get("/Welcome")
async def WelcomeMessage(settings: Settings = Depends(get_settings)):
    return f"Welcome to {settings.APP_NAME} v{settings.APP_VERSION}"

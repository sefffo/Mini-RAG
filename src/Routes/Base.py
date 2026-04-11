import os

from fastapi import FastAPI , APIRouter , status , HTTPException
# from dotenv import load_dotenv

router = APIRouter(prefix="/api/v1", tags=["Base"])


@router.get("/Welcome")
async def WelcomeMessage():
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')
    return f"Welcome to {app_name} v{app_version}"
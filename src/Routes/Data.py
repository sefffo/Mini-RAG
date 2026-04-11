from fastapi import APIRouter, Depends, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from src.Helpers.config import get_settings, Settings
from src.Controllers import DataController

Controller = DataController()
Data_router = APIRouter(prefix="/api/v1/Data", tags=["Data,V1"])


@Data_router.post("/upload/{Project_id}")
async def Upload(Project_id: str, file: UploadFile,
                 app_settings: Settings = Depends(get_settings)):
    # validations on the file frst
    isValid, signal = Controller.validateUploadedFile(file)
    if not isValid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": signal})
    # if valid then save the file

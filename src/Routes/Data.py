from fastapi import APIRouter, Depends, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from src.Helpers.config import get_settings, Settings
from src.Controllers import DataController
from src.Controllers import ProjectController
from src.Models.enums import responseEnum 
import os
import aiofiles
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

    # using the PRoject Contoller function

    project = ProjectController()

    project_dir_path = project.getProjectPath(projectId=Project_id)

    file_path = Controller.GenrateRandomFileName(file.filename, Project_id)
    # write it binary
    try:
        async with aiofiles.open(file_path, "wb") as f:
            # we gonna move chunk default size
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as ex:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": responseEnum.ResponseSignal.FILE_UPLOAD_FAILED.value, "details": str(ex)})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": signal})

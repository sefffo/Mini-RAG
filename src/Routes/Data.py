from fastapi import APIRouter, Depends , UploadFile
from src.Helpers.config import get_settings, Settings
from Controllers import DataController   

Controller = DataController()
Data_router = APIRouter(prefix="/api/v1/Data", tags=["Data,V1"])

@Data_router.post("/upload/{Project_id}")
async def Upload(Project_id:str,file : UploadFile,
                app_settings : Settings = Depends(get_settings)): 
    #validations on the file frst 
    isValid = Controller.validateUploadedFile(file)
    if not isValid:
        return {"error":"Invalid file. Please upload a valid file."  , "is_valid": isValid}
    #if valid then save the file
    
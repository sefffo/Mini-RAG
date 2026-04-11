from .BaseController import BaseContoller
from fastapi import UploadFile 
from src.Models import responseEnum
class DataController(BaseContoller):
    def __init__(self):
        super().__init__()


    #validate the data 
    def validateUploadedFile(self,file :UploadFile) -> tuple[bool,responseEnum.ResponseSignal]:
        #check the file type 
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False,responseEnum.ResponseSignal.FILE_TYPE_NOT_ALLOWED.value
        
        #check the file size 
        if file.size > self.app_settings.FILE_MAX_SIZE * 1024 * 1024:
            return False,responseEnum.ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True ,responseEnum.ResponseSignal.SUCCESS.value


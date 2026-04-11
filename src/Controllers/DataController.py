from .BaseController import BaseContoller
from fastapi import UploadFile 

class DataController(BaseContoller):
    def __int__(self):
        super().__int__()


    #validate the data 
    def validateUploadedFile(self,file :UploadFile)->bool:
        #check the file type 
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        
        #check the file size 
        if file.size > self.app_settings.FILE_MAX_SIZE * 1024 * 1024:
            return False
        
        return True


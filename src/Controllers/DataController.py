from .BaseController import BaseContoller
from fastapi import UploadFile
from src.Models import responseEnum
from src.Controllers import ProjectController
import re
import os


class DataController(BaseContoller):
    def __init__(self):
        super().__init__()

    # validate the data
    def validateUploadedFile(self, file: UploadFile) -> tuple[bool, responseEnum.ResponseSignal]:
        # check the file type
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, responseEnum.ResponseSignal.FILE_TYPE_NOT_ALLOWED.value

        # check the file size
        if file.size > self.app_settings.FILE_MAX_SIZE * 1024 * 1024:
            return False, responseEnum.ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, responseEnum.ResponseSignal.SUCCESS.value

    def GenrateRandomFileName(self, orginalFileName: str, projectId: str):
        randomFileName = self.generateRandomString()
        # get path of the project folder
        path = ProjectController.getProjectPath(projectId)

        cleanedFileName = self.getCleanFileName(orginalFileName)
        locatedFile = os.path.join(
            path,
            randomFileName + "_" + cleanedFileName
        )

        while os.path.exists(locatedFile):
            randomFileName = self.generateRandomString()
            locatedFile = os.path.join(
                path,
                randomFileName + "_" + cleanedFileName
            )

        return locatedFile

    def getCleanFileName(self, file_name: str) -> str:

        # remove any special characters, except underscore and
        cleaned_file_name = re.sub(r'[^\w.]', '', file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name

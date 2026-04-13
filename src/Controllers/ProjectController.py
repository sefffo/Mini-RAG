from .BaseController import BaseContoller
import os


class ProjectController(BaseContoller):
    def __init__():
        super().__init__()

    def getProjectPath(self, projectId):
        # create project directory first
        projectDir = os.path.join(
            self.filesUploadDir,
            projectId
        )
        # check if the project directory is not foumd we create it
        if not os.path.exists(projectDir):
            os.makedirs(projectDir)

        return projectDir

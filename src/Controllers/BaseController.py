from src.Helpers.config import get_settings , Settings
import os
class BaseContoller:
    def __init__(self): 
        self.app_settings = get_settings()
        self.BaseDir = os.path.dirname(os.path.abspath(__file__))

        self.filesUploadDir = os.path.join(self.BaseDir, "Assets/files")

from src.Helpers.config import get_settings , Settings
import os
import random
import string
import uuid
class BaseContoller:
    def __init__(self): 
        self.app_settings = get_settings()
        self.BaseDir = os.path.dirname(os.path.abspath(__file__))
        self.filesUploadDir = os.path.join(self.BaseDir, ".." ,"Assets/files")


    #generate random string
    # we can use it to generate random file name or random id for the project or any thing else
    def generateRandomString(self, length : int=12) -> str:
        letters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string    
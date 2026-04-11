from src.Helpers.config import get_settings , Settings

class BaseContoller:
    def __init__(self): 
        self.app_settings = get_settings()

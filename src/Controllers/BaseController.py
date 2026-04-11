from Helpers.config import get_settings , Settings

class BaseContoller:
    def __int__(self):
        self.app_settings = get_settings()

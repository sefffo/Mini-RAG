from dotenv import load_dotenv
load_dotenv(".env")

from fastapi import FastAPI
from src.Routes.Base import router as Base_Router
from src.Routes.Data import Data_router 

app = FastAPI()
app.include_router(Base_Router)
app.include_router(Data_router)

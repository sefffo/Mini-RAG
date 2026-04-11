from dotenv import load_dotenv
load_dotenv(".env")

from fastapi import FastAPI
from src.Routes.Base import router as Base_Router


app = FastAPI()
app.include_router(Base_Router)

from dotenv import load_dotenv
load_dotenv(".env")
from fastapi import FastAPI
from src.Routes.Base import router as Base_Router


app = FastAPI()
app.include_router(Base_Router)

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}   

# @app.get("/")
# async def WelcomeMessage():
#     return "Welcome on board"

# @app.get("/items/{itemid}")
# async def getProductById(itemid):
#     return {
#         "item" : itemid
#     }

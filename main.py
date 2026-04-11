from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/welcome")
async def WelcomeMessage():
    return "Welcome on board"

@app.get("/items/{itemid}")
async def getProductById(itemid):
    return {
        "item" : itemid
    }

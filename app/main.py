from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello world, welcome to gmak app w/ FastAPI"}

@app.get("/items/")
async def get_items():
    return {"item1": 14, "item2": 41}
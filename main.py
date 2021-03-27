from api import image_router
import uvicorn as uvicorn
from fastapi import FastAPI
from db import database, metadata, engine


app = FastAPI()
metadata.create_all(engine)
app.state.databases = database

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.databases
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.databases
    if database_.is_connected:
        await database_.disconnect()

app.include_router(image_router)






if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

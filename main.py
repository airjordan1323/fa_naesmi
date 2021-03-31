from api import news_router, partners_router
from event.api import events_router, history_router, org_router
from others.api import other_routers
from weather.api import another_router
import uvicorn as uvicorn
from fastapi import FastAPI
from db import database, metadata, engine


app = FastAPI()
# metadata.drop_all(engine)
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

app.include_router(news_router)
app.include_router(events_router)
app.include_router(history_router)
app.include_router(org_router)
app.include_router(other_routers)
app.include_router(partners_router)
app.include_router(another_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

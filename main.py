from graph import graph_router
from src.news.api import news_router, partners_router
from src.user.routers import user_router
from src.event.api import events_router, history_router, org_router
from src.others.api import other_routers
from src.weather.api import another_router
import uvicorn as uvicorn
from fastapi import FastAPI
from core.db import database, engine, metadata


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="Oav.uz | Naesmi",
    description="Oav.uz in FastAPI",
    version="1.0",
    openapi_url="/api/v1/openapi.json",
)

# ADD DELETE AND UPDATE ALL URLS

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
app.include_router(user_router)
app.include_router(graph_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

import shutil
from typing import List

from fastapi import APIRouter, UploadFile, File, Form

from .schemas import Message, CreateEvents, CreateHistory, CreateOrg
from .models import Events, History, Organization

events_router = APIRouter()
history_router = APIRouter()
org_router=APIRouter()

@events_router.post("/events")
async def create_events(
        title: str = Form(...),
        description: str = Form(...),
        location: str = Form(...),
        file: UploadFile = File(None)
):
    info = CreateEvents(title=title, description=description, location=location)
    with open(f'media/events/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return await Events.objects.create(file=file.filename, **info.dict())


@events_router.get("/events/{events_id}", response_model=Events, responses={404: {"model": Message}})
async def get_events(events_pk: int):
    return await Events.objects.get(pk=events_pk)


@events_router.get("/events-list", response_model=List[Events], responses={404: {"model": Message}})
async def get_events_list(lim: int = None, off: int = None):
    return await Events.objects.limit(lim).offset(off).all()


@history_router.post("/history")
async def make_history(i: CreateHistory):
    return await History.objects.create(**i.dict())


@history_router.get("/history_list", response_model=List[History], responses={404: {"model": Message}})
async def get_history_list(lim: int = None, off: int = None):
    return await History.objects.limit(lim).offset(off).all()


@org_router.post("/org")
async def add_org(
        name: str = Form(...),
        file: UploadFile = File(None)
):
    i = CreateOrg(name=name)
    with open(f'media/org/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return await Organization.objects.create(file=file.filename, **i.dict())


@org_router.get("/org-list", response_model=List[Organization], responses={404: {"model": Message}})
async def get_org_list():
    return await Organization.objects.all()



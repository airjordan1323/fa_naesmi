from datetime import datetime
from typing import List
from ..utils.services import load_image, ultimate_view
from fastapi import APIRouter, UploadFile, File, Form

from .schemas import Message, CreateEvents, CreateHistory, CreateOrg
from .models import Events, History, Organization

events_router = APIRouter(tags=["Events"])
history_router = APIRouter(tags=["History"])
org_router = APIRouter(tags=["Organizations"])


@events_router.post("/events")
async def create_events(
        title: str = Form(...),
        description: str = Form(...),
        location: str = Form(...),
        date: datetime = datetime.now(),
        file: UploadFile = File(None)
):
    info = CreateEvents(title=title, description=description, location=location,
                        date=date)
    if file is not None:
        file_name = f'media/news/{file.filename}'
        await load_image(file_name, file)
    else:
        file_name = None
    return await Events.objects.create(file=file_name, **info.dict())


@events_router.get("/events/{events_id}", response_model=Events, responses={404: {"model": Message}})
async def get_events(events_pk: int):
    return await Events.objects.get(pk=events_pk)


@events_router.get("/events-list", responses={404: {"model": Message}})
@ultimate_view
def get_events_list():
    return {"model": Events}


@history_router.post("/history")
async def make_history(i: CreateHistory):
    return await History.objects.create(**i.dict())


@history_router.get("/history_list", responses={404: {"model": Message}})
@ultimate_view
def get_history_list():
    return {"model": History}


@org_router.post("/org")
async def add_org(
        name: str = Form(...),
        file: UploadFile = File(None)
):
    i = CreateOrg(name=name)
    if file is not None:
        file_name = f'media/news/{file.filename}'
        await load_image(file_name, file)
    else:
        file_name = None
    return await Organization.objects.create(file=file_name, **i.dict())


@org_router.get("/org-list", response_model=List[Organization], responses={404: {"model": Message}})
async def get_org_list():
    return await Organization.objects.all()

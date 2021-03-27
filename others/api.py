import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form
from .schemas import *
from .models import *

other_routers = APIRouter()


@other_routers.post("/people")
async def add_people(
        position: str = Form(...),
        name: str = Form(...),
        first_name: str = Form(...),
        last_name: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(None)
):
    i = AddPeople(position=position, name=name, first_name=first_name,
                  last_name=last_name, description=description)
    with open(f'media/people/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return await People.objects.create(file=file.filename, **i.dict())


@other_routers.get("/people-list", response_model=List[People], responses={404: {"model": Message}})
async def get_people_list():
    return await People.objects.all()


@other_routers.post("/grants")
async def create_grants(
        title: str = Form(...),
        pers_name: str = Form(...),
        what: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(None)
):
    i = CreateGrants(title=title, pers_name=pers_name, what=what,
                     description=description)
    with open(f'media/grants/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return await Grants.objects.create(file=file.filename, **i.dict())


@other_routers.get("/grants-list", response_model=List[Grants], responses={404: {"model": Message}})
async def get_grants_list():
    return await Grants.objects.all()


@other_routers.post("/projects")
async def create_projects(
        name: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(None)
):
    i = CreateProjects(name=name, description=description)
    with open(f'media/projects/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return await Projects.objects.create(file=file.filename, **i.dict())


@other_routers.get("/projects-list", response_model=List[Projects], responses={404: {"model": Message}})
async def get_projects_list():
    return await Projects.objects.all()



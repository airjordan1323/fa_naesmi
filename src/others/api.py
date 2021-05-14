from typing import List
from fastapi import APIRouter, File, Form
from .models import *
from .schemas import *
from src.utils.services import *

other_routers = APIRouter()


@other_routers.post("/people", tags=["Peoples"])
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
    if file is not None:
        file_name = f'media/news/{file.filename}'
        await load_image(file_name, file)
    else:
        file_name = None
    return await People.objects.create(file=file_name, **i.dict())


@other_routers.get("/people-list", responses={404: {"model": Message}}, tags=["Peoples"])
def get_people_list():
    return {"model": People}


@other_routers.post("/grants", tags=["Grants"])
async def create_grants(
        title: str = Form(...),
        pers_name: str = Form(...),
        what: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(None)
):
    i = CreateGrants(title=title, pers_name=pers_name, what=what,
                     description=description)
    if file is not None:
        file_name = f'media/news/{file.filename}'
        await load_image(file_name, file)
    else:
        file_name = None
    return await Grants.objects.create(file=file_name, **i.dict())


@other_routers.get("/grants-list", responses={404: {"model": Message}}, tags=["Grants"])
@ultimate_view
def get_grants_list():
    return {"model": Grants}


@other_routers.post("/projects", tags=["Projects"])
async def create_projects(
        name: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(None)
):
    i = CreateProjects(name=name, description=description)
    if file is not None:
        file_name = f'media/news/{file.filename}'
        await load_image(file_name, file)
    else:
        file_name = None
    return await Projects.objects.create(file=file_name, **i.dict())


@other_routers.get("/projects-list", responses={404: {"model": Message}}, tags=["Projects"])
@ultimate_view
def project_list():
    return {"model": Projects}

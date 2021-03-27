import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form
from .schemas import *
from .models import *

people_routers = APIRouter()


@people_routers.post("/people")
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


@people_routers.get("/people-list", response_model=List[People], responses={404: {"model": Message}})
async def get_people_list():
    return await People.objects.all()



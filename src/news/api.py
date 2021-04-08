import shutil
from typing import List, Optional, Union
from uuid import uuid4
from ..utils.services import load_image, ultimate_view
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from .schemas import Message, AddPartners, CreateCategory, CreateNews
from .models import Category, News, Partners

news_router = APIRouter(tags=["News and Category"])
partners_router = APIRouter(tags=["Partners"])


@news_router.post("/category")
async def create_category(i: CreateCategory):
    return await Category.objects.create(**i.dict())


@news_router.get("/get-category", response_model=List[Category], responses={404: {"model": Message}})
async def get_category():
    return await Category.objects.all()


@news_router.post("/news")
async def create_news(
        title: str = Form(...),
        description: str = Form(...),
        category_id: int = Form(...),
        file: UploadFile = File(None)
):
    if file is not None:
        file_name = f'media/news/{category_id}_{uuid4()}.png'
        await load_image(file_name, file)

    else:
        file_name = None
    info = CreateNews(title=title, description=description)
    try:
        some = await Category.objects.get(id=category_id)
    except:
        return {"msg": "invalid category id"}
    return await News.objects.create(file=file_name, category=some, **info.dict())


@news_router.get("/news/{news_pk}", response_model=News, responses={404: {"model": Message}})
async def get_news(news_pk: int):
    return await News.objects.select_related('category').get(pk=news_pk)


@news_router.get("/news-list", responses={404: {"model": Message}})
@ultimate_view
def get_news_list():
    return {"model": News}


@partners_router.post("/partners")
async def add_partners(
        name: str = Form(...),
        file: UploadFile = File(None),
):
    i = AddPartners(name=name)
    with open(f'media/partners/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return await Partners.objects.create(file=file.filename, **i.dict())


@partners_router.get("/partners-list", responses={404: {"model": Message}})
@ultimate_view
def get_partners_list():
    return {"model": Partners}

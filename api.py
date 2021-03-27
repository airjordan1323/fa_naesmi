import shutil
from typing import List

from fastapi import APIRouter, UploadFile, File, Form

from schemas import Message, CreateNews, AddPartners
from models import *

news_router = APIRouter()
partners_router = APIRouter()


@news_router.post("/news")
async def create_news(
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(None)
):
    info = CreateNews(title=title, description=description)
    with open(f'media/news/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    category = await Category.objects.first()
    return await News.objects.create(file=file.filename, category=category, **info.dict())


@news_router.get("/news/{news_pk}", response_model=News, responses={404: {"model": Message}})
async def get_news(news_pk: int):
    return await News.objects.select_related('category').get(pk=news_pk)


@news_router.get("/news/", response_model=List[News], responses={404: {"model": Message}})
async def get_news_list():
    return await News.objects.select_related('category').all()


@partners_router.post("/partners")
async def add_partners(
        name: str = Form(...),
        file: UploadFile = File(None),
):
    i = AddPartners(name=name)
    with open(f'media/partners/{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return await Partners.objects.create(file=file.filename, **i.dict())


@partners_router.get("/partners-list", response_model=List[Partners], responses={404: {"model": Message}})
async def get_partners_list():
    return await Partners.objects.all()
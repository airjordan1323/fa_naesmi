import shutil
from typing import List, Optional
from uuid import uuid4

from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks, HTTPException
from .services import load_image
from .schemas import Message, AddPartners, CreateCategory, CreateNews
from .models import Category, News, Partners

news_router = APIRouter()
partners_router = APIRouter()


@news_router.post("/category")
async def create_category(i: CreateCategory):
    return await Category.objects.create(**i.dict())


@news_router.get("/get-category", response_model=List[Category], responses={404: {"model": Message}})
async def get_category():
    return await Category.objects.all()


@news_router.post("/news")
async def create_news(
        background_tasks: BackgroundTasks,
        title: str = Form(...),
        description: str = Form(...),
        category_id: int = Form(...),
        file: UploadFile = File(None)
):
    if file is not None:
        file_name = f'media/news/{category_id}_{uuid4()}.jpeg'
        if file.content_type == 'image/jpeg':
            # background_tasks.add_task(load_image, file_name, file)
            await load_image(file_name, file)
        else:
            raise HTTPException(status_code=418, detail="Это не формат изображений!")
    else:
        file_name = None
    info = CreateNews(title=title, description=description)
    try:
        some = await Category.objects.get(id=category_id)
    except:
        return {"msg": "invalid category id"}
    return await News.objects.create(file=file_name, category=some, **info.dict())
    # return await save_news(some.dict(), file, title, description, background_tasks)


@news_router.get("/news/{news_pk}", response_model=News, responses={404: {"model": Message}})
async def get_news(news_pk: int):
    return await News.objects.select_related('category').get(pk=news_pk)


@news_router.get("/news/", response_model=List[News], responses={404: {"model": Message}})
async def get_news_list(lim: int = None, off: int = 0, page: int = None, page_size: int = 10):
    if lim is not None:
        return await News.objects.limit(lim).offset(off).all()
    elif page is not None:
        return await News.objects.paginate(page, page_size).all()
    else:
        return await News.objects.all()


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
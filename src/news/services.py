import shutil

import aiofiles
from uuid import uuid4
from fastapi import UploadFile, HTTPException, BackgroundTasks, File
from src.news.schemas import CreateNews
from src.news.models import Category, News


async def save_news(
        category: str,
        file: UploadFile,
        title: str,
        description: str,
        background_tasks: BackgroundTasks):

    file_name = f'media/news/{category}_{uuid4()}.jpeg'
    background_tasks.add_task(load_image, file_name, file)
    await load_image(file_name, file)
    info = CreateNews(title=title, description=description)
    some = await Category.objects.create(name=category)
    return await News.objects.create(file=file.filename, category=some, **info.dict())


async def load_image(file_name: str = None, file: UploadFile = None):
    async with aiofiles.open(file_name, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)
    # with open(file_name, "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)


# async def lim_off_page(lim: int=None, off: int=None, page: int = None, page_size=None):
#     pass
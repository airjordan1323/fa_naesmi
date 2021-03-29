import aiofiles
import shutil
from uuid import uuid4
from fastapi import UploadFile, HTTPException, BackgroundTasks
from schemas import CreateNews
from models import *


async def save_news(
        category: str,
        file: UploadFile,
        title: str,
        description: str,
        background_tasks: BackgroundTasks):
    file_name = f'media/news/{category}_{uuid4()}.jpeg'
    if file.content_type == 'image/jpeg':
        # background_tasks.add_task(load_image, file_name, file)
        await load_image(file_name, file)
    else:
        raise HTTPException(status_code=418, detail="Это не формат изображений!")
    info = CreateNews(title=title, description=description)
    category = await Category.objects.first()
    return await News.objects.create(file=file.filename, category=category, **info.dict())


async def load_image(file_name: str, file: UploadFile):
    async with aiofiles.open(file_name, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)
    # with open(file_name, "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)
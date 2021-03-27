from typing import List
import shutil
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, BackgroundTasks

from schemas import UploadImage, GetImage, Message
from models import Image, User

image_router = APIRouter()


@image_router.post("/image")
async def create_image(
        background_tasks: BackgroundTasks,
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(None)
):
    file_name = f'media/{file.filename}'
    if file.content_type == 'video/mp4':
        background_tasks.add_task(write_video, file_name, file)
    else:
        raise HTTPException(status_code=418, detail="It isn't mp4")
    info = UploadImage(title=title, description=description)
    user = await User.objects.first()
    return await Image.objects.create(file=file.filename, user=user, **info.dict())


@image_router.get("/image/{image_pk}", response_model=Image, responses = {404: {"model": Message}})
async def get_image(image_pk: int):
    return await Image.objects.select_related('user').get(pk=image_pk)

import aiofiles
from uuid import uuid4
from fastapi import UploadFile, HTTPException, BackgroundTasks
from .schemas import UserOut
from .models import User


async def save_user(
        username: str,
        password: str,
        email: str,
        file: UploadFile,
        full_name: str,
        background_tasks: BackgroundTasks
):
    file_name = f'media/user/{username}_{uuid4()}.jpeg'
    if file.content_type == 'image/jpeg':
        await load_image(file_name, file)
    else:
        raise HTTPException(status_code=418, detail="Это не формат изображений!")
    info = UserOut(username=username, email=email, full_name=full_name)
    return await User.objects.create(file=file.filename, password=password, **info.dict())


async def load_image(file_name: str, file: UploadFile):
    async with aiofiles.open(file_name, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)

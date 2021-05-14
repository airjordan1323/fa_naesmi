from typing import List
from uuid import uuid4
import aiofiles
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from .services import load_image
from .schemas import Message, UserOut
from .models import *
from starlette.requests import Request
from .schemas import UserDB


def on_after_register(user: UserDB, request: Request) -> None:
    print(f"User {user.id} has registered.")


# def after_verification(user: UserDB, request: Request) -> None:
#     print(f"{user}")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


def after_verification_request(user: UserDB, token: str, request: Request) -> None:
    print(f"{user} - {token}")

# @user_router.post("/user/create")
# async def create_user(
#         username: str = Form(...),
#         password: str = Form(...),
#         full_name: str = Form(...),
#         email: str = Form(...),
#         file: UploadFile = File(None)
# ):
#     info = UserOut(username=username, email=email, full_name=full_name, password=password)
#     file_name = f'media/user/{username}_{uuid4()}.jpeg'
#     if file.content_type == 'image/jpeg':
#         await load_image(file_name, file)
#     else:
#         raise HTTPException(status_code=418, detail="Это не формат изображений!")
#     return await User.objects.create(file=file.filename, **info.dict())

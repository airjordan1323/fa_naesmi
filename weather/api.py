import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form
from .schemas import Message, PostContact, ApiWeather, PutContact
from .models import *


another_router = APIRouter()


@another_router.post("/contact")
async def post_contact(i: PostContact):
    return await Contact.objects.create(**i.dict())


@another_router.get("/contact-list", response_model=List[Contact], responses={404: {"model": Message}})
async def get_partners_list(lim: int = None, off: int = None):
    return await Contact.objects.limit(lim).offset(off).all()


@another_router.put("/contact-put/{contact_pk}", response_model=Contact)
async def put_contact(pk: int, contact: PutContact):
    entity = Contact(id=pk, **contact.dict())
    await entity.upsert()
    return entity





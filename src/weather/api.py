import fastapi
import httpx
import shutil
import requests
from typing import List
from fastapi import APIRouter, UploadFile, File, Form
from .schemas import Message, PostContact, ApiWeather, PutContact
from .models import *
from datetime import datetime

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


@another_router.get("/weathers", response_model=List[ApiWeather])
async def get_weathers():
    out = []
    new_weather = await get_forecast()
    for i in new_weather:
        out.append(await Weather(temperature=i[0], icon=i[1]).save())

    return out


@another_router.get("/wcheck", response_model=List[ApiWeather])
async def get_all():
    return await Weather.objects.all()


async def get_forecast():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=Tashkent&cnt=3&appid=da48613766e09300cf7c0cbeea366629&units=metric'
    res = requests.get(url).json()
    items = []
    for item in res['list']:
        temp = item['main']['temp']
        icon = f"https://openweathermap.org/img/wn/{item['weather'][0]['icon']}@2x.png"
        new_arr = [temp, icon]
        items.append(new_arr)
    return items

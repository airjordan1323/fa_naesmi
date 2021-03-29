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


@another_router.get("/weathers", response_model=ApiWeather)
async def get_weathers():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=Tashkent&cnt=3&appid=da48613766e09300cf7c0cbeea366629&units=metric'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    main = data.get('main', {})
    temp = main.get('temp', 0.0)

    weather = ApiWeather(temperature=temp)

    return weather





@another_router.get("/weather", response_model=ApiWeather)
async def get_weathers():
    queryset = Weather.objects.all()[:3]
    if len(queryset) == 3:
        item = queryset[0].pub_date
        now = datetime.datetime.now()
        if item.year <= now.year and item.day < now.day and item.month <=now.month:
            new_items = get_forecast()
            for delete in queryset:
                delete.delete()
            for we in new_items:
                Weather.objects.create(temperature=we[0])
            queryset = await Weather.objects.all()[:3]
        else:
            new_items = get_forecast()
            for we in new_items:
                Weather.objects.create(temperature=we[0])
            queryset = Weather.objects.all()[:3]

        return queryset


async def get_forecast():
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=Tashkent&cnt=3&appid=da48613766e09300cf7c0cbeea366629&units=metric'
    res = await requests.get(url).json()
    items = []
    for item in res['list']:
        temp = item['main']['temp']
        new_arr = [temp]
        items.append(new_arr)
    return items
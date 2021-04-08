import requests
from typing import List
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from .schemas import Message, PostContact, ApiWeather, PutContact
from .models import *

another_router = APIRouter()


@another_router.post("/contact", tags=["Contacts"])
async def post_contact(i: PostContact):
    return await Contact.objects.create(**i.dict())


@another_router.get("/contact-list", response_model=List[Contact], responses={404: {"model": Message}}, tags=["Contacts"])
async def get_partners_list(lim: int = None, off: int = None, checked: bool = None):
    if lim is not None:
        try:
            return await Contact.objects.limit(lim).all()
        except:
            return await Contact.objects.offset(off).all()
    if checked is not None:
        try:
            return await Contact.objects.limit(lim).offset(off).filter(checked=checked).all()
        except:
            return await Contact.objects.filter(checked=checked).all()
        # finally:
        #     raise HTTPException(status_code=418, detail="Фильтрация по таким параметрам невозможно!"
        #                                             " Убедитесь что правильно ввели данные!")
    else:
        return await Contact.objects.all()

@another_router.put("/contact-put/{contact_pk}", response_model=Contact, tags=["Contacts"])
async def put_contact(pk: int, contact: PutContact):
    entity = Contact(id=pk, **contact.dict())
    await entity.upsert()
    return entity


@another_router.get("/weathers", response_model=List[ApiWeather], tags=["Weather"])
async def get_weathers():
    out = []
    new_weather = await get_forecast()
    for i in new_weather:
        out.append(await Weather(temperature=i[0], icon=i[1]).save())

    return out


@another_router.get("/wcheck", response_model=List[ApiWeather], tags=["Weather"])
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

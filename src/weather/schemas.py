from pydantic import BaseModel
import datetime


class Message(BaseModel):
    message: str


class ApiWeather(BaseModel):
    temperature: float
    icon: str
    pub_date: datetime.datetime


class PostContact(BaseModel):
    title: str
    face: str
    phone: str
    email: str
    message: str


class PutContact(BaseModel):
    # id: int
    title: str
    face: str
    phone: str
    email: str
    message: str
    checked: bool

from pydantic import BaseModel


class Message(BaseModel):
    message: str


class ApiWeather(BaseModel):
    temperature: float


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
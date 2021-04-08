from datetime import datetime

from pydantic import BaseModel

class CreateEvents(BaseModel):
    title: str
    description: str
    location: str
    date: datetime


class CreateHistory(BaseModel):
    description: str
    date: datetime


class CreateOrg(BaseModel):
    name: str


class Message(BaseModel):
    message: str
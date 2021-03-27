from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str


class CreateNews(BaseModel):
    title: str
    description: str


class AddPartners(BaseModel):
    name: str


class Message(BaseModel):
    message: str

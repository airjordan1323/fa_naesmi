from pydantic import BaseModel


class CreateCategory(BaseModel):
    # id: int
    name: str


class CreateNews(BaseModel):
    title: str
    description: str


class AddPartners(BaseModel):
    name: str


class Message(BaseModel):
    message: str

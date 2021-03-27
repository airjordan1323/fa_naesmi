from pydantic import BaseModel

class Status(BaseModel):
    message: str

class User(BaseModel):
    id: int
    username: str


class UploadImage(BaseModel):
    title: str
    description: str


class GetImage(BaseModel):
    user: User
    title: str
    description: str


class Message(BaseModel):
    message: str

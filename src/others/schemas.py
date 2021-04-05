from pydantic import BaseModel


class AddPeople(BaseModel):
    position: str
    name: str
    first_name: str
    last_name: str
    description: str


class CreateGrants(BaseModel):
    title: str
    pers_name: str
    what: str
    description: str


class CreateProjects(BaseModel):
    name: str
    description: str


class Message(BaseModel):
    message: str
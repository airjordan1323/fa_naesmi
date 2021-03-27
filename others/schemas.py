from pydantic import BaseModel


class AddPeople(BaseModel):
    position: str
    name: str
    first_name: str
    last_name: str
    description: str


# class CreateGrants(BaseModel):



class Message(BaseModel):
    message: str
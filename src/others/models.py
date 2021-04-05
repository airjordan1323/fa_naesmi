import datetime
import ormar
from core.db import MainMeta


class People(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    position: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    name: str = ormar.String(max_length=100)
    first_name: str = ormar.String(max_length=100)
    last_name: str = ormar.String(max_length=100)
    description: str = ormar.String(max_length=100)


class Grants(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=150)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    pers_name: str = ormar.String(max_length=300)
    what: str = ormar.String(max_length=1000)
    description: str = ormar.String(max_length=100)
    file: str = ormar.String(max_length=1000)


class Projects(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    description: str = ormar.String(max_length=100)
    file: str = ormar.String(max_length=1000)
    # url: str = ormar.String(max_length=1000)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    # last_change: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
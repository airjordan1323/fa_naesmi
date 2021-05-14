import datetime
import ormar
from core.db import MainMeta


class Events(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=300)
    description: str = ormar.String(max_length=100)
    location: str = ormar.String(max_length=100)
    file: str = ormar.String(max_length=1000, nullable=True)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)


class History(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    description: str = ormar.String(max_length=100)
    date: datetime.datetime = ormar.DateTime()


class Organization(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    file: str = ormar.String(max_length=1000)

import datetime
from typing import Optional

import ormar
from db import database, metadata


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Category(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)


class News(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=70)
    description: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    pub_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    # last_change: datetime.datetime = ormar.DateTime()
    category: Optional[Category] = ormar.ForeignKey(Category)


class Partners(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=50)
    file: str = ormar.String(max_length=1000)
    # url: str = ormar.String(max_length=1000)
    pub_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    # last_change: datetime.datetime = ormar.DateTime()


class People(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    position: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    name: str = ormar.String(max_length=100)
    first_name: str = ormar.String(max_length=100)
    last_name: str = ormar.String(max_length=100)
    description: str = ormar.String()


class History(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    description: str = ormar.String()
    date: datetime.datetime = ormar.DateTime()

class Grants(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=150)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    pers_name: str = ormar.String(max_length=300)
    what: str = ormar.String(max_length=1000)
    description: str = ormar.String()
    file: str = ormar.String(max_length=1000)


class Projects(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    description: str = ormar.String()
    file: str = ormar.String(max_length=1000)
    # url: str = ormar.String(max_length=1000)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    # last_change: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())


class Events(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=300)
    description: str = ormar.String()
    location: str = ormar.String()
    file: str = ormar.String(max_length=1000)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    # url: str = ormar.String(max_length=1000)


class Organization(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=150)
    file: str = ormar.String(max_length=1000)
    # url: str = ormar.String(max_length=1000)

class Weather(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    icon: str = ormar.String(max_length=250)
    temperature: int = ormar.Integer()
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())


class Contact(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=150)
    face: str = ormar.String(max_length=150)
    phone: str = ormar.String(max_length=15)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    email: str = ormar.String(max_length=100)
    message: str = ormar.String()
    checked: bool = ormar.Boolean(default=False)



import datetime
import ormar
from typing import Optional
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
    title: str = ormar.String(max_length=170)
    description: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=1000)
    pub_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
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


#
#
# class Weather(ormar.Model):
#     class Meta(MainMeta):
#         pass
#
#     id: int = ormar.Integer(primary_key=True)
#     icon: str = ormar.String(max_length=250)
#     temperature: int = ormar.Integer()
#     date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
#
#
# class Contact(ormar.Model):
#     class Meta(MainMeta):
#         pass
#
#     id: int = ormar.Integer(primary_key=True)
#     title: str = ormar.String(max_length=150)
#     face: str = ormar.String(max_length=150)
#     phone: str = ormar.String(max_length=15)
#     date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
#     email: str = ormar.String(max_length=100)
#     message: str = ormar.String(max_length=100)
#     checked: bool = ormar.Boolean(default=False)



import datetime
import ormar
from typing import Optional
from core.db import MainMeta


# class MainMeta(ormar.ModelMeta):
#     metadata = metadata
#     database = database


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
    file: str = ormar.String(max_length=1000, nullable=True)
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


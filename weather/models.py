import datetime
import ormar
from models import MainMeta


class Weather(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    temperature: float = ormar.Float()
    icon: str = ormar.String(max_length=150)
    pub_date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)


class Contact(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=150)
    face: str = ormar.String(max_length=150)
    phone: str = ormar.String(max_length=15)
    date: datetime.datetime = ormar.DateTime(default=datetime.datetime.now())
    email: str = ormar.String(max_length=100)
    message: str = ormar.String(max_length=100)
    checked: bool = ormar.Boolean(default=False)
import ormar
from core.db import MainMeta
from fastapi_users.db import OrmarUserDatabase, OrmarBaseUserModel
from src.user.schemas import UserDB

class User(OrmarBaseUserModel):
    class Meta(MainMeta):
        pass


    username: str = ormar.String(max_length=100, unique=True)
    phone: str = ormar.String(max_length=14, unique=True)


user_db = OrmarUserDatabase(UserDB, User)


    # id: int = ormar.Integer(primary_key=True)
    # username: str = ormar.String(max_length=30)
    # password: str = ormar.String(max_length=50)
    # file: str = ormar.String(max_length=1000)
    # full_name: str = ormar.String(max_length=100)
    # email: str = ormar.String(max_length=100)
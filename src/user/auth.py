from fastapi_users.authentication import JWTAuthentication
from fastapi_users import FastAPIUsers
from .models import user_db
from .schemas import User, UserDB, UserCreate, UserUpdate


SECRET = "BHIVGIVBKLJBytspfpuh1438a7089;ASAEPIUHAGH312839ASFNsdfgsdg"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600,
                                       tokenUrl="/auth/jwt/login")

auth_backends.append(jwt_authentication)


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB
)

current_active_user = fastapi_users.current_user(active=True)
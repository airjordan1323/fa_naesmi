from fastapi import APIRouter
from .api import on_after_register, after_verification_request, \
    on_after_forgot_password
from .auth import jwt_authentication, fastapi_users, SECRET


user_router = APIRouter()


user_router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
user_router.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)
user_router.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)
user_router.include_router(
    fastapi_users.get_verify_router(
        SECRET,
        after_verification_request=after_verification_request), prefix="/auth", tags=["auth"])

user_router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])

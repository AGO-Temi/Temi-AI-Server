from fastapi import APIRouter

from .service import UserService

user_router = APIRouter()


@user_router.get("/socialmedia", status_code=200)
def socialmedia():
    return UserService.getExampleUserInformation()

from fastapi import APIRouter

from .service import ChatService

chat_router = APIRouter()


@chat_router.post("/", status_code=200)
def socialmedia():
    return ChatService.getExampleUserInformation()

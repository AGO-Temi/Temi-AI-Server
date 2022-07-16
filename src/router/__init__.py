from fastapi import APIRouter


from .chat import chat_router

router = APIRouter()


router.include_router(
    chat_router,
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

router_list = [{"router": chat_router, "prefix": "/user"}]

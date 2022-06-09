from fastapi import APIRouter


from .user import user_router

router = APIRouter()


@router.get("/test")
def test():
    return "success for test"


router.include_router(
    user_router,
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

router_list = [{"router": user_router, "prefix": "/user"}]

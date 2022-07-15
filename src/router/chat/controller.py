from fastapi import APIRouter

from .model import QuestionReq, QuestionRes

from .service import ChatService

chat_router = APIRouter()


@chat_router.post("/", status_code=200)
def getQuestion(req : QuestionReq) -> QuestionRes:
    return ChatService.getQuestion(req)


@chat_router.get("/", status_code=200)
def getQuestionList():
    return ChatService.getQuestionList()
    
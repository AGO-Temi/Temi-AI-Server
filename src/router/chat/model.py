from pydantic import BaseModel


class QuestionReq(BaseModel):
    place: int
    question: str


class QuestionRes(BaseModel):
    answer: str

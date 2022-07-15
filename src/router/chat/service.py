from multiprocessing.connection import answer_challenge
from src.ai.models.chatbot import ChatBot

from src.constant import question
from .model import QuestionReq, QuestionRes

ai = ChatBot(question)


class ChatService:
    @staticmethod
    def getQuestion(req: QuestionReq) -> QuestionRes:
        ai.setPlace(req.place)
        answer = ai.question(req.question)
        return {"answer": answer}

    @staticmethod
    def getQuestionList() -> QuestionRes:
        questionList = ai.make_recommended_questions()
        return {"answerList": questionList}

from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: str
    difficulty: str
    explanation: str
    related_topics: List[str]

class Quiz(BaseModel):
    quiz_title: str
    questions: List[Question]

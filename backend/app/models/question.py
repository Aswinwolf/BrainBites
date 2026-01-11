from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from app.core.database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    question = Column(Text, nullable=False)
    options = Column(JSONB, nullable=False)
    correct_answer = Column(Text, nullable=False)
    difficulty = Column(Text)
    explanation = Column(Text)
    related_topics = Column(JSONB)

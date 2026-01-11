from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("wikipedia_articles.id"))
    quiz_title = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

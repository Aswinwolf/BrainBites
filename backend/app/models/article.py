from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class WikipediaArticle(Base):
    __tablename__ = "wikipedia_articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    summary = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.quiz import Quiz
from app.models.article import WikipediaArticle

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    data = (
        db.query(Quiz.id, Quiz.quiz_title, WikipediaArticle.title)
        .join(WikipediaArticle, Quiz.article_id == WikipediaArticle.id)
        .order_by(Quiz.id.desc())
        .all()
    )

    return [
        {
            "quiz_id": q.id,
            "quiz_title": q.quiz_title,
            "article_title": q.title
        }
        for q in data
    ]

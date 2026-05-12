from sqlalchemy.orm import Session
from typing import Optional
from ..models.flower import Flower
from ..schemas.flower import FlowerCreate


class FlowerService:
    @staticmethod
    def get_flowers(db: Session, offset: int = 0, limit: int = 10, category: Optional[str] = None):
        query = db.query(Flower)
        if category:
            query = query.filter(Flower.category == category)

        total = query.count()
        items = query.order_by(Flower.create_time.desc()).offset(offset).limit(limit).all()
        return total, items

    @staticmethod
    def get_flower_by_id(db: Session, flower_id: int) -> Optional[Flower]:
        return db.query(Flower).filter(Flower.id == flower_id).first()

    @staticmethod
    def create_flower(db: Session, flower: FlowerCreate) -> Flower:
        db_flower = Flower(**flower.model_dump())
        db.add(db_flower)
        db.commit()
        db.refresh(db_flower)
        return db_flower

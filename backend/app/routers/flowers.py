from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from ..database import get_db
from ..schemas.flower import FlowerResponse, FlowerListResponse
from ..services.flower import FlowerService

router = APIRouter(prefix="/api/flowers", tags=["flowers"])


@router.get("", response_model=FlowerListResponse)
def get_flowers(
    offset: int = Query(0, ge=0, description="起始位置"),
    limit: int = Query(10, ge=1, le=100, description="查询数量"),
    category: Optional[str] = Query(None, description="分类筛选"),
    db: Session = Depends(get_db)
):
    total, items = FlowerService.get_flowers(db, offset=offset, limit=limit, category=category)
    return FlowerListResponse(total=total, items=items)


@router.get("/{flower_id}", response_model=FlowerResponse)
def get_flower(flower_id: int, db: Session = Depends(get_db)):
    flower = FlowerService.get_flower_by_id(db, flower_id)
    if not flower:
        raise HTTPException(status_code=404, detail="Flower not found")
    return flower

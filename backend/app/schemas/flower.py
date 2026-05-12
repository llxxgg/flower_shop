from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class FlowerBase(BaseModel):
    name: str
    price: float
    image: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None


class FlowerCreate(FlowerBase):
    pass


class FlowerResponse(FlowerBase):
    id: int
    create_time: datetime

    model_config = ConfigDict(from_attributes=True)


class FlowerListResponse(BaseModel):
    total: int
    items: list[FlowerResponse]

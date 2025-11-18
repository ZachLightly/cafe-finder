from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import List
from ..item.schemas import ItemResponse

class CafePatch(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    cafe_rating: Optional[float] = None
    menu_rating: Optional[float] = None
    image_url: Optional[str] = None

class CafePost(BaseModel):
    name: str
    location: str
    cafe_rating: float
    menu_rating: float
    image_url: str

class CafeResponse(CafePost):
    id: UUID
    items: List[ItemResponse]

    model_config = ConfigDict(from_attributes=True)

class CafeListResponse(BaseModel):
    cafes: list[CafeResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
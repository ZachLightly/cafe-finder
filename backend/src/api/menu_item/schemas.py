from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID

class MenuItemPatch(BaseModel):
    name: Optional[str] = None
    name_slug: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    average_rating: Optional[float] = None
    ratings_count: Optional[float] = None
    image_url: Optional[str] = None
    cafe_id: Optional[UUID] = None

class MenuItemPost(BaseModel):
    name: str
    name_slug: str
    description: Optional[str] = ""
    price: Optional[float] = 0.0
    image_url: Optional[str] = ""
    cafe_id: UUID

class MenuItemResponse(MenuItemPost):
    name: str
    name_slug: str
    description: str
    price: float
    average_rating: float
    ratings_count: float
    image_url: str
    cafe_id: UUID

    model_config = ConfigDict(from_attributes=True)

class MenuItemListResponse(BaseModel):
    items: list[MenuItemResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
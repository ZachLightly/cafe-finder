from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import List
from ..menu_item.schemas import MenuItemResponse
from .address import Address

class CafePatch(BaseModel):
    name: Optional[str] = None
    address: Optional[Address] = None
    cafe_rating: Optional[float] = None
    menu_rating: Optional[float] = None
    image_url: Optional[str] = None

class CafePost(BaseModel):
    name: str
    address: Address
    category: str
    image_url: str

class CafeResponse(CafePost):
    id : UUID 
    name : str
    name_slug : str
    address: Address
    address_id: UUID
    
    cafe_rating: float
    cafe_rating_count: float
    menu_rating: float
    menu_rating_count: float
    image_url: str
    category: str
    menu: List[MenuItemResponse]

    model_config = ConfigDict(from_attributes=True)

class CafeListResponse(BaseModel):
    cafes: list[CafeResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
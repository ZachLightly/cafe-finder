from pydantic import BaseModel, ConfigDict
from uuid import UUID

class CafeRequest(BaseModel):
    name: str
    location: str
    cafe_rating: float
    menu_rating: float
    image_url: str

class CafeResponse(CafeRequest):
    id: UUID
    
    model_config=ConfigDict(from_attributes=True)
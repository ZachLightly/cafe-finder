from pydantic import BaseModel, ConfigDict
from uuid import UUID

class ItemPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    rating: float | None = None
    notes: str | None = None
    image_url: str | None = None
    cafe_id: UUID | None = None

class ItemPost(BaseModel):
    name: str
    description: str = ""
    rating: float
    notes: str = ""
    image_url: str = ""
    cafe_id: UUID

class ItemResponse(ItemPost):
    id: UUID

    model_config = ConfigDict(from_attributes=True)

class ItemListResponse(BaseModel):
    items: list[ItemResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
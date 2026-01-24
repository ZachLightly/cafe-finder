from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import List
from ..menu_item.schemas import ItemResponse

class Address(BaseModel):
    id = UUID
    street = str
    city = str
    state = str
    zip_code = str
    latitude = float
    longitude = float
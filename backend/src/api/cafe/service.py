from ...core.db import SessionDep
from .repo import CafeRepo
from .schemas import CafeResponse
from typing import List
from uuid import UUID

class CafeService:
    def __init__(self, db: SessionDep):
        self.repo = CafeRepo(db)
        
    def get_all(self) -> List[CafeResponse]:
        orm_cafes = self.repo.get_all()
        return [CafeResponse.model_validate(c) for c in orm_cafes]
    
    def get_by_id(self, cafe_id: UUID) -> CafeResponse:
        orm_cafe = self.repo.get_by_id(cafe_id)
        return CafeResponse.model_validate(orm_cafe) if orm_cafe else None
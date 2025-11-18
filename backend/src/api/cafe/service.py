from ...core.db import SessionDep
from .repo import CafeRepo
from .schemas import CafeResponse, CafeListResponse, CafePost, CafePatch
from uuid import UUID
from fastapi import HTTPException

class CafeService:
    def __init__(self, db: SessionDep):
        self.repo = CafeRepo(db)
        
    def get_all(self,
                rating: float | None = None,
                page: int = 1,
                page_size: int = 20
                ) -> CafeListResponse:
        offset = (page - 1) * page_size
        orm_cafes, total = self.repo.get_all(
            limit=page_size, 
            offset=offset, 
            rating=rating
            )
        cafes = [CafeResponse.model_validate(orm_cafe) for orm_cafe in orm_cafes]
        
        total_pages = (total + page_size - 1) // page_size
        return CafeListResponse(
            cafes=cafes,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )

    def get_by_id(self, cafe_id: UUID) -> CafeResponse | None:
        orm_cafe = self.repo.get_by_id(cafe_id)
        if orm_cafe is None:
            raise HTTPException(status_code=404, detail="Cafe not found")
        return CafeResponse.model_validate(orm_cafe)
    
    def get_by_name(self, name: str) -> CafeResponse | None:
        orm_cafe = self.repo.get_by_name(name)
        if orm_cafe is None:
            raise HTTPException(status_code=404, detail="Cafe not found")
        return CafeResponse.model_validate(orm_cafe)

    def get_by_location(self, location: str) -> CafeResponse | None:
        orm_cafe = self.repo.get_by_location(location)
        if orm_cafe is None:
            raise HTTPException(status_code=404, detail="Cafe not found")
        return CafeResponse.model_validate(orm_cafe)
    
    def create(self, cafe: CafePost) -> CafeResponse:
        orm_cafe = self.repo.create(cafe)
        return CafeResponse.model_validate(orm_cafe)
    
    def update_by_id(self, cafe_id: UUID, cafe: CafePatch) -> CafeResponse | None:
        orm_cafe = self.repo.update_by_id(cafe_id, cafe)
        return CafeResponse.model_validate(orm_cafe) if orm_cafe else None
    
    def delete_by_id(self, cafe_id: UUID) -> CafeResponse | None:
        orm_cafe = self.repo.delete_by_id(cafe_id)
        return CafeResponse.model_validate(orm_cafe) if orm_cafe else None
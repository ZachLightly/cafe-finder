from ...core.db import SessionDep
from typing import List
from uuid import UUID
from ...core.models.cafe import Cafe
from .schemas import CafePost, CafePatch

class CafeRepo:
    def __init__(self, db: SessionDep):
        self.db = db
        
    def get_by_id(self, cafe_id: UUID) -> Cafe | None:
        return self.db.query(Cafe).filter(Cafe.id == cafe_id).first()
    
    
    def get_by_name(self, name: str) -> Cafe | None:
        return self.db.query(Cafe).filter(Cafe.name.ilike(f"%{name}%")).first()
    
    
    def get_by_location(self, location: str) -> Cafe | None:
        return self.db.query(Cafe).filter(Cafe.location.ilike(f"%{location}%")).first()
    
        
    def get_all(self,
                limit: int = 20,
                offset: int = 0,
                rating: float | None = None,
                ) -> tuple[List[Cafe], int]:
        query = self.db.query(Cafe)
        if rating is not None:
            query = query.filter(Cafe.cafe_rating >= rating).order_by(Cafe.cafe_rating.desc())
    
        total = query.count()
        
        cafes = query.offset(offset).limit(limit).all()
        
        return cafes, total
    
    def create(self, data: CafePost) -> Cafe:
        cafe = Cafe(**data)
        self.db.add(cafe)
        self.db.commit()
        self.db.refresh(cafe)
        return cafe

    def update_by_id(self, cafe_id: UUID, data: CafePatch) -> Cafe | None:
        existing_cafe = self.get_by_id(cafe_id)
        if not existing_cafe:
            return None

        for key, value in data.model_dump().items():
            if key == "id" or value is None:
                continue
            if hasattr(existing_cafe, key):
                setattr(existing_cafe, key, value)

        try:
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        self.db.refresh(existing_cafe)
        print(existing_cafe)
        print(data)
        return existing_cafe
    
    def delete_by_id(self, cafe_id: UUID) -> Cafe | None:
        cafe = self.get_by_id(cafe_id)
        if not cafe:
            return None

        self.db.delete(cafe)
        self.db.commit()
        return cafe
    
    
        
        

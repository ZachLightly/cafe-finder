from ...core.db import SessionDep
from typing import List
from uuid import UUID
from ...core.models.cafe import Cafe

class CafeRepo:
    def __init__(self, db: SessionDep):
        self.db = db
        
    # TODO: full file: no error checking
        
    def get_by_id(self, cafe_id: UUID) -> Cafe:
        return self.db.query(Cafe).filter(Cafe.id == cafe_id).first()
    
    def get_all(self) -> List[Cafe]:
        return self.db.query(Cafe).all()
    
    def create(self, data: dict) -> Cafe:
        cafe = Cafe(**data)
        self.db.add(cafe)
        self.db.commit()
        self.db.refresh(cafe)
        return cafe
    
    def update_by_id(self, cafe_id: UUID, data: dict) -> Cafe:
        old_cafe = self.get_by_id(cafe_id)
        if not old_cafe:
            return None

        for key, value in data.items():
            if key == "id":
                continue
            if hasattr(old_cafe, key):
                setattr(old_cafe, key, value)

        self.db.commit()
        self.db.refresh(old_cafe)
        return old_cafe
        

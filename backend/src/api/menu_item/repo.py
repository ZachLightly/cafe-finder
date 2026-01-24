from ...core.db import SessionDep
from typing import List
from uuid import UUID
from ...core.models.menu_item import MenuItem
from .schemas import ItemPost, MenuItemPatch, ItemListResponse

class ItemRepo:
    def __init__(self, db: SessionDep):
        self.db = db
        
    def get_by_id(self, item_id: UUID) -> MenuItem | None:
        return self.db.query(MenuItem).filter(MenuItem.id == item_id).first()
    
    
    def get_by_name(self, name: str) -> MenuItem | None:
        # TODO: better logic for similar name: slug?
        return self.db.query(MenuItem).filter(MenuItem.name.ilike(f"%{name}%")).first()
    
    
    def get_all_by_cafe_id(self, cafe_id: str) -> List[MenuItem]:
        return self.db.query(MenuItem).filter(MenuItem.cafe_id == cafe_id).all()
    
        
    def get_all(self,
                limit: int = 20,
                offset: int = 0,
                rating: float | None = None,
                ) -> tuple[List[MenuItem], int]:
        query = self.db.query(MenuItem)
        if rating is not None:
            query = query.filter(MenuItem.average_rating >= rating).order_by(MenuItem.average_rating.desc())
    
        total = query.count()
        
        cafes = query.offset(offset).limit(limit).all()
        
        return cafes, total
    
    def create(self, data: ItemPost) -> MenuItem:
        item = MenuItem(**data.model_dump())
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update_by_id(self, item_id: UUID, data: MenuItemPatch) -> MenuItem | None:
        existing_item = self.get_by_id(item_id)
        if not existing_item:
            return None

        for key, value in data.model_dump().items():
            if key == "id" or value is None:
                continue
            if hasattr(existing_item, key):
                setattr(existing_item, key, value)

        try:
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
        self.db.refresh(existing_item)
        return existing_item
    
    def delete_by_id(self, item_id: UUID) -> MenuItem | None:
        item = self.get_by_id(item_id)
        if not item:
            return None

        self.db.delete(item)
        self.db.commit()
        return item
    
    
        
        

from ...core.db import SessionDep
from .repo import ItemRepo
from .schemas import ItemPost, MenuItemPatch, ItemResponse, ItemListResponse
from uuid import UUID
from fastapi import HTTPException

class ItemService:
    def __init__(self, db: SessionDep):
        self.repo = ItemRepo(db)
        
    def get_all(self,
                rating: float | None = None,
                page: int = 1,
                page_size: int = 20
                ) -> ItemListResponse:
        offset = (page - 1) * page_size
        orm_items, total = self.repo.get_all(
            limit=page_size, 
            offset=offset, 
            rating=rating
            )
        items = [ItemResponse.model_validate(orm_item) for orm_item in orm_items]
        
        total_pages = (total + page_size - 1) // page_size
        return ItemListResponse(
            items=items,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )

    def get_by_id(self, item_id: UUID) -> ItemResponse | None:
        orm_item = self.repo.get_by_id(item_id)
        if orm_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return ItemResponse.model_validate(orm_item)
    
    def get_by_name(self, name: str) -> ItemResponse | None:
        orm_Item = self.repo.get_by_name(name)
        if orm_Item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return ItemResponse.model_validate(orm_Item)

    def get_all_by_cafe_id(self, cafe_id: str) -> ItemResponse | None:
        orm_items = self.repo.get_all_by_cafe_id(cafe_id)
        return [ItemResponse.model_validate(orm_item) for orm_item in orm_items]
    
    def create(self, item: ItemPost) -> ItemResponse:
        orm_item = self.repo.create(item)
        return ItemResponse.model_validate(orm_item)
    
    def update_by_id(self, item_id: UUID, item: MenuItemPatch) -> ItemResponse | None:
        orm_item = self.repo.update_by_id(item_id, item)
        return ItemResponse.model_validate(orm_item) if orm_item else None
    
    def delete_by_id(self, item_id: UUID) -> ItemResponse | None:
        orm_item = self.repo.delete_by_id(item_id)
        return ItemResponse.model_validate(orm_item) if orm_item else None
from typing import List
from fastapi import APIRouter, Query
from ...core.db import SessionDep
from .service import ItemService
from .schemas import ItemPost, MenuItemPatch, ItemResponse, ItemListResponse
from uuid import UUID


router = APIRouter(
    prefix="/items",
    tags=["Items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=ItemListResponse)
async def get_items(
    db: SessionDep,
    rating: float | None = Query(None, ge=1, le=5, description="Filter by rating"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page")
):
    service = ItemService(db)
    return service.get_all(
        rating=rating,
        page=page, 
        page_size=page_size
    )
    
@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(db: SessionDep, item_id: UUID):
    service = ItemService(db)
    return service.get_by_id(item_id)

@router.get("/by-name/{name}", response_model=ItemResponse)
async def get_item_by_name(db: SessionDep, name: str):
    service = ItemService(db)
    return service.get_by_name(name)

@router.get("/by-cafe/{cafe_id}", response_model=List[ItemResponse])
async def get_items_by_cafe_id(db: SessionDep, cafe_id: UUID):
    service = ItemService(db)
    return service.get_all_by_cafe_id(cafe_id)

@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(db: SessionDep, item: ItemPost):
    service = ItemService(db)
    return service.create(item)

@router.patch("/{item_id}", response_model=ItemResponse)
async def update_item(db: SessionDep, item_id: UUID, item: MenuItemPatch):
    service = ItemService(db)
    return service.update_by_id(item_id, item)

@router.delete("/{item_id}", response_model=ItemResponse)
async def delete_item(db: SessionDep, item_id: UUID):
    service = ItemService(db)
    return service.delete_by_id(item_id)
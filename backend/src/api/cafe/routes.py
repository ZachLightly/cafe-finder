from fastapi import APIRouter, Query
from ...core.db import SessionDep
from .service import CafeService
from .schemas import CafeResponse, CafePost, CafePatch, CafeListResponse
from uuid import UUID


router = APIRouter(
    prefix="/cafes",
    tags=["Cafes"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=CafeListResponse)
async def get_cafes(
    db: SessionDep,
    rating: float | None = Query(None, ge=1, le=5, description="Filter by rating"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page")
):
    service = CafeService(db)
    return service.get_all(
        rating=rating,
        page=page, 
        page_size=page_size
    )
    
@router.get("/{cafe_id}", response_model=CafeResponse)
async def get_cafe(db: SessionDep, cafe_id: UUID):
    service = CafeService(db)
    return service.get_by_id(cafe_id)

@router.get("/by-name/{name}", response_model=CafeResponse)
async def get_cafe_by_name(db: SessionDep, name: str):
    service = CafeService(db)
    return service.get_by_name(name)

@router.get("/by-location/{location}", response_model=CafeResponse)
async def get_cafe_by_location(db: SessionDep, location: str):
    service = CafeService(db)
    return service.get_by_location(location)

@router.post("/", response_model=CafeResponse, status_code=201)
async def create_cafe(db: SessionDep, cafe: CafePost):
    service = CafeService(db)
    return service.create(cafe)

@router.patch("/{cafe_id}", response_model=CafeResponse)
async def update_cafe(db: SessionDep, cafe_id: UUID, cafe: CafePatch):
    service = CafeService(db)
    return service.update_by_id(cafe_id, cafe)

@router.delete("/{cafe_id}", response_model=CafeResponse)
async def delete_cafe(db: SessionDep, cafe_id: UUID):
    service = CafeService(db)
    return service.delete_by_id(cafe_id)
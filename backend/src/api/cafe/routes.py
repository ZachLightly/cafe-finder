from fastapi import APIRouter
from ...core.db import SessionDep
from .service import CafeService
from typing import List
from .schemas import CafeResponse, CafeRequest

router = APIRouter(
    prefix="/cafes",
    tags=["Cafes"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[CafeResponse])
async def get_cafes(db: SessionDep):
    service = CafeService(db)
    cafes = service.get_all()
    return cafes

@router.post("/", response_model=CafeResponse, status_code=201)
async def create_cafe(db: SessionDep, cafe: CafeRequest):
    service = CafeService(db)
    cafe_out = service.create(cafe)
    
    return cafe_out
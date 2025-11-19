from typing import List
from fastapi import APIRouter, Query
from ...core.db import SessionDep
from .service import UserService
from .schemas import UserRegister, UserResponse
from uuid import UUID


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)
    
@router.get("/{user_id}", response_model=UserResponse)
async def get_user(db: SessionDep, user_id: UUID):
    service = UserService(db)
    return service.get_by_id(user_id)
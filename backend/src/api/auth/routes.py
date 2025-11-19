from fastapi import APIRouter, Depends, HTTPException

from ..user.schemas import UserRegister, UserResponse
from ..user.service import UserService
from backend.src.core.db import SessionDep
from .auth import OAuth2PasswordRequestForm
from .schemas import Token
from typing import Annotated

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)



@router.post("/token", response_model=Token)
async def login_for_access_token(db: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    service = UserService(db)
    return await service.login_for_access_token(form_data.username, form_data.password)

@router.post("/register", response_model=UserResponse)
async def register(db: SessionDep, data: UserRegister):
    service = UserService(db)
    return await service.register_user(data)


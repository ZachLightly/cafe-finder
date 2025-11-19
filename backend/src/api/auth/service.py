from ...core.db import SessionDep
from ..user.service import UserService
from fastapi import HTTPException, status
from . import auth
from .schemas import Token
from ..user.schemas import UserRegister, UserResponse

class AuthService:
    def __init__(self, db: SessionDep):
        self.user_service = UserService(db)

    async def login_for_access_token(self, username: str, password: str) -> Token:
        user = auth.authenticate_user(self.user_service, username, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = auth.create_access_token(user.username, user.id)
        return Token(access_token=access_token)

    async def register_user(self, data: UserRegister) -> UserResponse:
        existing_user = self.user_service.get_by_username(data.username)
        if existing_user:
            raise HTTPException(status_code=400, detail="Username not available")
        data.password = auth.get_password_hash(data.password)
        user = self.user_service.create_user(data)
        return UserResponse.model_validate(user)
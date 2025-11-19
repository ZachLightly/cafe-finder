from ...core.db import SessionDep
from .repo import UserRepo
from .schemas import UserRegister, UserResponse
from uuid import UUID
from fastapi import HTTPException

class UserService:
    def __init__(self, db: SessionDep):
        self.repo = UserRepo(db)

    def get_by_id(self, user_id: UUID) -> UserResponse:
        orm_user = self.repo.get_by_id(user_id)
        if orm_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse.model_validate(orm_user)
    
    def get_by_username(self, username: str) -> UserResponse:
        orm_user = self.repo.get_by_username(username)
        if orm_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse.model_validate(orm_user)
    
    def get_by_email(self, email: str) -> UserResponse:
        orm_user = self.repo.get_by_email(email)
        if orm_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse.model_validate(orm_user)
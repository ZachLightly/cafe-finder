from ...core.db import SessionDep
from typing import List
from uuid import UUID
from ...core.models.user import User
from .schemas import UserRegister, UserPatch

class UserRepo:
    def __init__(self, db: SessionDep):
        self.db = db
        
    def get_by_id(self, user_id: UUID) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()
    
    def get_by_username(self, username: str) -> User | None:
        return self.db.query(User).filter(User.username == username).first()
    
    def create_user(self, data: UserRegister) -> User:
        user = User(
            username=data.username,
            email=data.email,
            hashed_password=data.password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def update_user(self, data: UserPatch) -> User:
        self.db.commit()
        self.db.refresh(user)
        return user
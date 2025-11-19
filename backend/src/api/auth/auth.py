from datetime import datetime, timedelta, timezone
from uuid import UUID

from ...core.db import SessionDep
from .schemas import TokenData
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from typing import Annotated
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from os import getenv
from dotenv import load_dotenv
from ..user.repo import UserRepo

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
  
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

def authenticate_user(user_repo: UserRepo, username: str, password: str):
    user = user_repo.get_by_username(username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: UUID, expires_delta: timedelta = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {
        "sub": username,
        "id": str(user_id),
        "exp": expire
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        user_id = payload.get("id")
        if username is None:
            raise credentials_exception
        return TokenData(username=username, user_id=user_id)
    except InvalidTokenError:
        raise credentials_exception

def get_user(db: SessionDep, username: str):
    user_repo = UserRepo(db)
    return user_repo.get_by_username(username)

async def get_current_user(db: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]):
    token_data = decode_token(token)
    user = get_user(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user
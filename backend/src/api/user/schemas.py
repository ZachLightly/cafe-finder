from pydantic import BaseModel

class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    
class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    pfp_url: str | None = None
    bio: str | None = None
    location: str | None = None
    
class UserPatch(BaseModel):
    pfp_url: str | None = None
    bio: str | None = None
    location: str | None = None
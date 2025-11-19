from sqlalchemy import Column, String, Float, ForeignKey, UUID
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import UUID
from ..db import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    pfp_url = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    location = Column(String, nullable=True)
    visits = relationship("Visit", back_populates="user", cascade="all, delete-orphan")
    
from datetime import datetime
from sqlalchemy import Column, DateTime, String, Float, ForeignKey, UUID
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import UUID
from ..db import Base
import uuid

class Visit(Base):
    __tablename__ = "visits"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    cafe_id = Column(UUID(as_uuid=True), ForeignKey("cafes.id"), nullable=False, index=True)
    rating = Column(Float, nullable=True)
    comment = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.now())

    user = relationship("User", back_populates="visits")
    cafe = relationship("Cafe", back_populates="visits")
    
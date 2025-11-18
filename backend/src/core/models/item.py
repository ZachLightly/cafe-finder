from sqlalchemy import Column, Integer, String, Float, ForeignKey, UUID
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import UUID
from ..db import Base
import uuid

class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    description = Column(String)
    rating = Column(Float)
    notes = Column(String)
    image_url = Column(String)
    # cafe
    cafe_id = Column(UUID(as_uuid=True), ForeignKey("cafes.id"), nullable=False, index=True)
    cafe = relationship("Cafe", back_populates="items")
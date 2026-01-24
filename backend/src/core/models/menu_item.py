from sqlalchemy import Column, String, Float, ForeignKey, UUID
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import UUID
from ..db import Base
import uuid

class MenuItem(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    name_slug = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    average_rating = Column(Float)
    ratings_count = Column(Float, default=0)
    image_url = Column(String)
    # cafe
    cafe_id = Column(UUID(as_uuid=True), ForeignKey("cafes.id"), nullable=False, index=True)
    cafe = relationship("Cafe", back_populates="items")
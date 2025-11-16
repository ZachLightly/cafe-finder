from sqlalchemy import Column, Integer, String, Float, UUID
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.sqlite import UUID
from ..db import Base
import uuid

class Cafe(Base):
    __tablename__ = "cafes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    location = Column(String, index=True)
    cafe_rating = Column(Float)
    menu_rating = Column(Float)
    image_url = Column(String)
    # array of menu items
    items = relationship("Item", back_populates="cafe", cascade="all, delete-orphan")
    
    
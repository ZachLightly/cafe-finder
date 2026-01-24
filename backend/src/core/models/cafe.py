from sqlalchemy import Column, ForeignKey, Integer, String, Float, UUID
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.sqlite import UUID
from ..db import Base
import uuid

class Cafe(Base):
    __tablename__ = "cafes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    name_slug = Column(String, index=True)
    address = relationship("Address", back_populates="cafe", uselist=False, cascade="all, delete-orphan")
    address_id = Column(UUID(as_uuid=True), ForeignKey("addresses.id"), nullable=False, index=True)
    
    cafe_rating = Column(Float)
    cafe_rating_count = Column(Float, default=0)
    menu_rating = Column(Float)
    menu_rating_count = Column(Float, default=0)
    image_url = Column(String)
    category = Column(String)
    
    # array of menu items
    menu = relationship("MenuItem", back_populates="cafe", cascade="all, delete-orphan")
    
    
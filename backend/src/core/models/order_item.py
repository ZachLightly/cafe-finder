from sqlalchemy import Column, ForeignKey, Integer, String, Float, UUID
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.sqlite import UUID
from ..db import Base
import uuid

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    visit_id = Column(UUID(as_uuid=True), ForeignKey("visits.id"), nullable=False, index=True)
    menu_item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False, index=True)
    quantity = Column(Integer, default=1)
    
    notes = Column(String, nullable=True)
    rating = Column(Float, nullable=True)
    image_url = Column(String, nullable=True)
    # array of menu items
    visit = relationship("Visit", back_populates="order_items")
    menu_item = relationship("MenuItem")
    
    
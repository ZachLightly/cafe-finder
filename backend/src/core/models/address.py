from sqlalchemy import Column, Integer, String, Float, UUID
from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.sqlite import UUID
from ..db import Base
import uuid

class Address(Base):
    __tablename__ = "cafes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    street = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    zip_code = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    
    
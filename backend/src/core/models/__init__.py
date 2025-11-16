# src/core/models/__init__.py
# Import each model module so the mapped classes are registered with SQLAlchemy
from .cafe import Cafe
from .item import Item

__all__ = ["Cafe", "Item"]
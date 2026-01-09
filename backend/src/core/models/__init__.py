# src/core/models/__init__.py
# Import each model module so the mapped classes are registered with SQLAlchemy
from .cafe import Cafe
from .menu_item import MenuItem

__all__ = ["Cafe", "MenuItem"]
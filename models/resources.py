#!/usr/bin/python3
"""This defines the resource model"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class Resources(BaseModel, Base):
    """this defines the resources table"""

    __tablename__ = "resources"

    class_room_id = Column(String(60), ForeignKey("class_rooms.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    title = Column(String(60), nullable=False)
    notes = Column(String(60))
    resource_link = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes resources"""
        super().__init__(*args, **kwargs)

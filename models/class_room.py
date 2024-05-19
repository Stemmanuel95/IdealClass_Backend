#!/usr/bin/python3
"""This defines the assignment model"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class ClassRoom(BaseModel, Base):
    """this defines the classrooms table"""

    __tablename__ = "class_rooms"

    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(60))
    assignments = relationship(
        "Assignment",
        backref="class_room",
        cascade="all, delete, delete-orphan",
    )
    resources = relationship("Resources", backref="class_room", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes classroom"""
        super().__init__(*args, **kwargs)

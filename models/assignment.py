#!/usr/bin/python3
"""This defines the assignment model"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class Assignment(BaseModel, Base):
    """this defines the assingment table"""

    __tablename__ = "assignments"

    class_room_id = Column(String(60), ForeignKey("class_rooms.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    title = Column(String(60), nullable=False)
    notes = Column(String(60))
    resource_link = Column(String(60))
    submitted_assignments = relationship(
        "SubmittedAssignment",
        backref="assignment",
        cascade="all, delete, delete-orphan",
    )

    def __init__(self, *args, **kwargs):
        """initializes assignment"""
        super().__init__(*args, **kwargs)

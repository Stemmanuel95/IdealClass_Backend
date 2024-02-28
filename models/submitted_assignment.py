#!/usr/bin/python3
"""This defines a submitted assignment model
"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class SubmittedAssignment(BaseModel, Base):
    """this defines the submitted_assgnments table"""

    __tablename__ = "submitted_assignments"

    assignment_id = Column(String(60), ForeignKey("assignments.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    title = Column(String(60), nullable=False)
    notes = Column(String(60))
    resource_link = Column(String(250))

    def __init__(self, *args, **kwargs):
        """initializes submitted assingments"""
        super().__init__(*args, **kwargs)

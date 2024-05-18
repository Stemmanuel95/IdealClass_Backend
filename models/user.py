#!/usr/bin/env python3
"""This module cover User Model
"""
from enum import Enum as PythonEnum

from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class RoleEnum(PythonEnum):
    TEACHER = "teacher"
    STUDENT = "student"


class User(BaseModel, Base):
    """User Model"""

    __tablename__ = "users"

    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.TEACHER)
    reset_token = Column(String(250), nullable=True)
    class_rooms = relationship("ClassRoom", backref="user", cascade="all, delete, delete-orphan")
    assignments = relationship("Assignment", backref="user", cascade="all, delete, delete-orphan")
    submitted_assignments = relationship(
        "SubmittedAssignment",
        backref="user",
        cascade="all, delete, delete-orphan",
    )
    resources = relationship("Resources", backref="user", cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

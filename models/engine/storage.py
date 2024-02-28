#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound

import models
from models.assignment import Assignment
from models.base_model import Base
from models.class_room import ClassRoom
from models.resources import Resources
from models.submitted_assignment import SubmittedAssignment
from models.user import User

classes = {
    "ClassRoom": ClassRoom,
    "User": User,
    "Assignment": Assignment,
    "Resources": Resources,
    "SubmittedAssignment": SubmittedAssignment,
}


class DBStorage:
    """This class interacts with the MYSQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        load_dotenv()
        IDEAL_CLASS_DATABASE_URI = getenv(
            "SQLALCHEMY_DATABASE_URI",
            "postgresql://postgres:password@localhost:5432/idealclass",
        )
        self.__engine = create_engine(IDEAL_CLASS_DATABASE_URI)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class
        and its ID, or None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        obj = next((value for value in all_cls.values() if value.id == id), None)
        return obj

    def count(self, cls=None):
        """
        Returns the number of objects in storage matching the given class
        If no class is passed, returns the count of all objects in storage
        """
        if not cls:
            return len(models.storage.all())
        else:
            return len(models.storage.all(cls))

    def find_user_by(self, **kwargs) -> User:
        """returns the first row found in the users table as
        filtered by the method’s input arguments
        """
        if not kwargs:
            raise (InvalidRequestError)
        user = self.__session.query(User).filter_by(**kwargs).first()
        if not user:
            raise (NoResultFound)
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """update the user’s attributes as passed in the method’s
        arguments then commit changes to the database
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)

        self.__session.commit()

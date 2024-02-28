#!/usr/bin/python3
"""
This Handles all the api Restful actions for Reviews
"""
from flask import abort, jsonify

from api.v1.routes import app_routes
from models import storage
from models.class_room import ClassRoom
from models.user import User


@app_routes.route("/classrooms", methods=["GET"], strict_slashes=False)
def get_class_rooms():
    """This retrieves a list all classes"""

    class_rooms = [class_room.to_dict() for class_room in storage.all(ClassRoom).values()]
    return class_rooms


@app_routes.route("users/<user_id>/classrooms", methods=["GET"], strict_slashes=False)
def get_class_room(user_id):
    """This retrieves a list all classrooms of a particular teacher user"""

    user = storage.get(User, user_id)
    if not user:
        abort(404)
    class_rooms = [class_room.to_dict() for class_room in user.classrooms]
    return class_rooms

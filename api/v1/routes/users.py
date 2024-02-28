#!/usr/bin/env python3
"""
Starts A flask App
"""
from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt, jwt_required

from api.v1.error import (
    bad_request,
    forbidden_error,
    not_found,
    unauthorized_error,
)
from api.v1.routes import AUTH, app_routes
from models import storage
from models.user import User


@app_routes.route("/users", methods=["GET"], strict_slashes=False)
@jwt_required()
def get_users():
    """This retrieves a list all users"""
    user_list = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(user_list)


@app_routes.route("/users", methods=["POST"], strict_slashes=False)
def register_users() -> str:
    """Registers new user"""
    user_data = request.get_json()
    role = user_data.get("role").upper()
    required_role = ["STUDENT", "TEACHER"]
    if role not in required_role:
        return bad_request("Wrong role assignment, TEACHER OR STUDENT needed")
    try:
        new_user = AUTH.register_user(**user_data)
    except ValueError:
        return jsonify({"message": "email already registered"})

    return jsonify(new_user.to_dict())


@app_routes.route("/users/login", methods=["POST"], strict_slashes=False)
def login() -> str:
    """Logs in a user"""
    user_data = request.get_json()

    email = user_data.get("email")
    password = user_data.get("hashed_password")

    if not AUTH.valid_login(email, password):
        return unauthorized_error()

    access_token = AUTH.create_session(email)
    response = jsonify({"email": email, "access_token": access_token, "message": "logged in"}), 200
    return response


@app_routes.route("/users/logout", methods=["DELETE"], strict_slashes=False)
@jwt_required()
def logout() -> str:
    """logs the user out"""
    access_token = get_jwt()["jti"]
    if access_token:
        AUTH.destroy_session(access_token)
        return make_response(jsonify({"message": "successfully loggeout"}), 200)
    else:
        return forbidden_error()


@app_routes.route("/users/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """Gets reset password token"""
    user_data = request.get_json()

    email = user_data.get("email")
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except Exception:
        return forbidden_error()
    return make_response(jsonify({"email": email, "reset_token": reset_token}), 201)


@app_routes.route("/users/update_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """Updates password"""

    user_data = request.get_json()

    email = user_data.get("email")
    password = user_data.get("new_password")
    reset_token = user_data.get("reset_token")

    required = ["email", "new_password", "reset_token"]

    for data in required:
        if data not in user_data.keys():
            return bad_request(f"{data} missing")
    try:
        AUTH.update_password(reset_token, password)
    except Exception:
        return forbidden_error()

    return make_response(jsonify({"email": email, "message": "Password updated"}), 201)


@app_routes.route("/users/<user_id>", methods=["PATCH"], strict_slashes=False)
@jwt_required()
def put_user(user_id):
    """Updates a particular users's attributes"""
    user = storage.get(User, user_id)
    if not user:
        return not_found("User")

    user_data = request.get_json()
    if not user_data:
        return bad_request()

    ignore_list = ["first_name", "last_name"]

    for key, value in user_data.items():
        if key in ignore_list:
            setattr(user, key, value)
        else:
            return bad_request(f"Cannot update {key}")

    storage.save()
    return make_response(jsonify(user.to_dict()), 200)


@app_routes.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
@jwt_required()
def delete_user(user_id):
    """Deletes a paticular customer object"""

    user = storage.get(User, user_id)
    if not user:
        return not_found("User")

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)

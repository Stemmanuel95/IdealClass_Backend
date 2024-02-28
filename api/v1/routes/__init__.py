#!/usr/bin/python3
from flask import Blueprint

from api.v1.auth import Auth
from api.v1.routes.classrooms import *
from api.v1.routes.users import *

AUTH = Auth()

app_routes = Blueprint("app_routes", __name__, url_prefix="/api/v1")

#!/usr/bin/python3
from os import getenv

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from api.v1.auth import BLACK_LIST_TOKEN
from api.v1.routes import app_routes
from models import storage

app = Flask(__name__)

app.register_blueprint(app_routes)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.config["JWT_SECRET_KEY"] = getenv("JWT_SECRET_KEY", "you-cant-see-me")
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_blacklist(jwt_header, jwt_data):
    jti = jwt_data["jti"]
    return jti in BLACK_LIST_TOKEN


@app.teardown_appcontext
def close_db(self):
    """This closes the database session"""
    storage.close()


if __name__ == "__main__":
    app.run(threaded=True, debug=True)

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.from_object(config)
        config.init_app(app)

    jwt.init_app(app)

    db.init_app(app)

    migrate.init_app(app)

    CORS(app)

    # from .api import api as api_blueprint

    # app.register_blueprint(api_blueprint, url_prefix="/api")

    # from .auth import auth as auth_blueprint

    # app.register_blueprint(auth_blueprint, url_prefix="/auth")

    # from .main import main as main_blueprint

    # app.register_blueprint(main_blueprint)

    from .models import models

    models.init_app(app)

    return app, models


# @app.route("/")
# def hello_world():
#     return {"Message": "IdealClass"}

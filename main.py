# from app import jwt
# from app import db
from os import getenv

from app import create_app
from config import config

app = create_app(config["development"])

# @app.shell_context_processor
# def make_shell_context():
#     return {
#         "jwt": jwt,
#         "db": db
#     }

if __name__ == "__main__":
    host = getenv("HOST", "0.0.0.0")
    port = getenv("PORT", 5000)
    app.run(host=host, port=port)

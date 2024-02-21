from app import app
from os import getenv

if __name__ == "__main__":
    host = getenv("HOST", "0.0.0.0")
    port = getenv("PORT", 5000)
    app.run(host=host, port=port)

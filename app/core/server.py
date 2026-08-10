from waitress import serve

from app.core import create_app
from app.core.config import settings

app = create_app()


if __name__ == "__main__":
    print(f"DevOps Market Python em http://localhost:{settings.port}")
    serve(app, host="0.0.0.0", port=settings.port)

from pathlib import Path

from app.core.config import settings
from scripts.seed_database import main as seed


def sqlite_path() -> Path:
    return Path(settings.database_url.removeprefix("sqlite:///"))


def main() -> None:
    db_path = sqlite_path()
    if db_path.exists():
        db_path.unlink()
    seed()


if __name__ == "__main__":
    main()

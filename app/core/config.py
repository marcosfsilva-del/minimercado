import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///data/devops_market.db")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    commit_sha: str = os.getenv("COMMIT_SHA", "local")
    secret_key: str = os.getenv("SECRET_KEY", "devops-market-local")
    port: int = int(os.getenv("PORT", "3000"))


settings = Settings()

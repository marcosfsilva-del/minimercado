import os
import sys

import requests

BASE_URL = os.getenv("SMOKE_BASE_URL", f"http://localhost:{os.getenv('PORT', '3000')}")

CHECKS = [
    ("frontend", "/"),
    ("backend", "/api"),
    ("health", "/api/health"),
    ("catálogo", "/api/products"),
]


def main() -> None:
    for name, path in CHECKS:
        response = requests.get(f"{BASE_URL}{path}", timeout=5)
        if response.status_code >= 400:
            print(f"FAIL {name}: {response.status_code} {path}")
            sys.exit(1)
        print(f"OK {name}: {path}")


if __name__ == "__main__":
    main()

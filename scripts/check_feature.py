import re
import sys
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z][a-z0-9-]*$")


def main() -> None:
    if len(sys.argv) != 2 or not SLUG_RE.match(sys.argv[1]):
        print("Uso: python3 tasks.py feature-check product-search")
        sys.exit(1)

    slug = sys.argv[1]
    feature_dir = Path("app/features") / slug.replace("-", "_")
    checks = [
        feature_dir / "manifest.py",
        feature_dir / "routes.py",
        feature_dir / "service.py",
        feature_dir / "templates",
        feature_dir / "tests",
        feature_dir / "README.md",
    ]

    failed = False
    for path in checks:
        exists = path.exists()
        print(f"{'OK' if exists else 'FAIL'} {path}")
        failed = failed or not exists

    if failed:
        sys.exit(1)

    print(f"Feature '{slug}' segue a estrutura minima.")


if __name__ == "__main__":
    main()

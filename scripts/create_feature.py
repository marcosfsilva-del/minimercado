import re
import sys
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z][a-z0-9-]*$")


def class_name(slug: str) -> str:
    return "".join(part.capitalize() for part in slug.split("-"))


def main() -> None:
    if len(sys.argv) != 2 or not SLUG_RE.match(sys.argv[1]):
        print("Uso: python3 tasks.py feature-create product-search")
        print("Slug: letras minusculas, numeros e hifens.")
        sys.exit(1)

    slug = sys.argv[1]
    py_name = slug.replace("-", "_")
    feature_dir = Path("app/features") / py_name
    if feature_dir.exists():
        print(f"A feature '{slug}' ja existe.")
        sys.exit(1)

    feature_dir.mkdir(parents=True)
    (feature_dir / "templates").mkdir()
    (feature_dir / "tests").mkdir()
    title = slug.replace("-", " ").title()

    (feature_dir / "__init__.py").write_text('"""Feature gerada."""\n', encoding="utf-8")
    (feature_dir / "service.py").write_text(
        f'''def status() -> dict[str, str]:
    return {{"feature": "{slug}", "status": "ok"}}
''',
        encoding="utf-8",
    )
    (feature_dir / "routes.py").write_text(
        f'''from flask import Blueprint, jsonify, render_template

from app.features.{py_name}.service import status

bp = Blueprint("{py_name}", __name__, url_prefix="/{slug}", template_folder="templates")


@bp.get("")
def page():
    return render_template("{slug}.html")


@bp.get("/api")
def api():
    return jsonify(status())
''',
        encoding="utf-8",
    )
    (feature_dir / "manifest.py").write_text(
        f'''from app.core.types.features import FeatureManifest, MenuItem
from app.features.{py_name}.routes import bp

manifest = FeatureManifest(
    id="{slug}",
    name="{title}",
    blueprint=bp,
    menu=MenuItem(label="{title}", endpoint="{py_name}.page", order=50),
    slots=[],
)
''',
        encoding="utf-8",
    )
    (feature_dir / "templates" / f"{slug}.html").write_text(
        f'''{{% extends "base.html" %}}

{{% block content %}}
<section class="page-title">
  <div>
    <h2>{title}</h2>
    <p>Feature em desenvolvimento.</p>
  </div>
</section>
{{% endblock %}}
''',
        encoding="utf-8",
    )
    (feature_dir / "tests" / f"test_{py_name}.py").write_text(
        f'''from app.features.{py_name}.service import status


def test_status():
    assert status() == {{"feature": "{slug}", "status": "ok"}}
''',
        encoding="utf-8",
    )
    (feature_dir / "README.md").write_text(f"# {title}\n\nDescreva a feature.\n", encoding="utf-8")

    print(f"Feature criada: {slug}")
    print(f"Pasta Python: {feature_dir}")


if __name__ == "__main__":
    main()

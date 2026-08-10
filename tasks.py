import argparse
import os
import subprocess
import sys


def run(command: list[str], env: dict[str, str] | None = None) -> None:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    completed = subprocess.run(command, env=merged_env, check=False)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(description="Tarefas do DevOps Market")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("dev")
    sub.add_parser("lint")
    sub.add_parser("test")
    sub.add_parser("build")
    sub.add_parser("docker-build")
    sub.add_parser("smoke")
    sub.add_parser("db-seed")
    sub.add_parser("db-reset")

    create = sub.add_parser("feature-create")
    create.add_argument("slug")

    check = sub.add_parser("feature-check")
    check.add_argument("slug")

    args = parser.parse_args()

    if args.command == "dev":
        run([sys.executable, "-m", "app.core.server"])
    elif args.command == "lint":
        run([sys.executable, "-m", "ruff", "check", "."])
    elif args.command == "test":
        run([sys.executable, "-m", "pytest"])
    elif args.command == "build":
        run([sys.executable, "-m", "compileall", "-q", "app", "scripts", "tasks.py"])
    elif args.command == "docker-build":
        run(["docker", "build", "-t", "devops-market-python", "."])
    elif args.command == "smoke":
        run([sys.executable, "-m", "scripts.smoke_test"])
    elif args.command == "db-seed":
        run([sys.executable, "-m", "scripts.seed_database"])
    elif args.command == "db-reset":
        run([sys.executable, "-m", "scripts.reset_database"])
    elif args.command == "feature-create":
        run([sys.executable, "-m", "scripts.create_feature", args.slug])
    elif args.command == "feature-check":
        run([sys.executable, "-m", "scripts.check_feature", args.slug])


if __name__ == "__main__":
    main()

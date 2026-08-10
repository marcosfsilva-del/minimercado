from importlib import import_module
from pathlib import Path

from flask import Flask

from app.core.types.features import SLOT_NAMES, FeatureManifest, SlotContribution


class FeatureRegistry:
    def __init__(self) -> None:
        self.manifests: list[FeatureManifest] = []

    def discover(self, include_example: bool = False) -> list[FeatureManifest]:
        features_dir = Path(__file__).resolve().parents[1] / "features"
        manifests: list[FeatureManifest] = []

        for directory in sorted(features_dir.iterdir()):
            if not directory.is_dir() or directory.name.startswith("__"):
                continue
            if directory.name == "_example" and not include_example:
                continue

            module = import_module(f"app.features.{directory.name}.manifest")
            manifest = getattr(module, "manifest", None)
            self._validate_manifest(directory.name, manifest)
            manifests.append(manifest)

        self.manifests = manifests
        return manifests

    def register_blueprints(self, app: Flask) -> None:
        for manifest in self.manifests:
            if manifest.blueprint:
                app.register_blueprint(manifest.blueprint)

    def menu_items(self):
        return sorted(
            [manifest.menu for manifest in self.manifests if manifest.menu],
            key=lambda item: item.order,
        )

    def slot_renderers(self, slot: str) -> list[SlotContribution]:
        return [
            contribution
            for manifest in self.manifests
            for contribution in manifest.slots
            if contribution.slot == slot
        ]

    @staticmethod
    def _validate_manifest(directory_name: str, manifest: object) -> None:
        if not isinstance(manifest, FeatureManifest):
            raise ValueError(
                f"Invalid feature manifest: {directory_name}. Missing manifest object."
            )
        if not manifest.id:
            raise ValueError(f"Invalid feature manifest: {directory_name}. Missing field: id.")
        if not manifest.name:
            raise ValueError(f"Invalid feature manifest: {directory_name}. Missing field: name.")
        for contribution in manifest.slots:
            if contribution.slot not in SLOT_NAMES:
                raise ValueError(
                    "Invalid feature manifest: "
                    f"{directory_name}. Invalid slot: {contribution.slot}."
                )


registry = FeatureRegistry()

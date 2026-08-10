from collections.abc import Callable
from dataclasses import dataclass, field

from flask import Blueprint

SLOT_NAMES = {
    "PRODUCT_LIST_TOOLBAR",
    "PRODUCT_CARD",
    "CART_ITEM",
    "CART_SUMMARY",
    "CHECKOUT_FORM",
    "ORDER_SUMMARY",
    "MAIN_MENU",
    "DASHBOARD",
}


@dataclass(frozen=True)
class MenuItem:
    label: str
    endpoint: str
    order: int = 50


@dataclass(frozen=True)
class SlotContribution:
    slot: str
    renderer: Callable[..., str]


@dataclass(frozen=True)
class FeatureManifest:
    id: str
    name: str
    blueprint: Blueprint | None = None
    menu: MenuItem | None = None
    slots: list[SlotContribution] = field(default_factory=list)

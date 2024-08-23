from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Effect,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.items.item import Item


@dataclass
class ItemFlingEffect(CommonResource):
    effect_entries: List["Effect"]
    items: List["NamedAPIResource[Item]"]

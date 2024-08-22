from dataclasses import dataclass
from typing import List

from aiopoke.models.items.item import Item
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Effect,
)


@dataclass
class ItemFlingEffect(CommonResource):
    effect_entries: List[Effect]
    items: List[NamedAPIResource["Item"]]

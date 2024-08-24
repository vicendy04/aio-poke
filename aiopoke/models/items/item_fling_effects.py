from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        effect_entries: List[Dict[str, Any]],
        items: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.effect_entries = (
            [Effect(**entry) for entry in effect_entries] if effect_entries else []
        )
        self.items = [NamedAPIResource(**item) for item in items] if items else []

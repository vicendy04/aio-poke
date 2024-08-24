from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.items.item_categories import ItemCategory
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


@dataclass
class ItemPocket(CommonResource):
    categories: List["NamedAPIResource[ItemCategory]"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        categories: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.categories = (
            [NamedAPIResource(**category) for category in categories]
            if categories
            else []
        )
        self.names = [Name(**name) for name in names] if names else []

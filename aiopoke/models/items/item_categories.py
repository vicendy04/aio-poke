from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.items.item import Item
    from aiopoke.models.items.item_pockets import ItemPocket


class ItemCategory(CommonResource):
    items: List["NamedAPIResource[Item]"]
    names: List["Name"]
    pocket: NamedAPIResource["ItemPocket"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        items: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        pocket: Dict[str, Any],
    ) -> None:
        super().__init__(id=id, name=name)
        self.items = [NamedAPIResource(**item) for item in items] if items else []
        self.names = [Name(**name) for name in names] if names else []
        self.pocket = NamedAPIResource(**pocket)

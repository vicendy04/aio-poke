from typing import TYPE_CHECKING, List

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

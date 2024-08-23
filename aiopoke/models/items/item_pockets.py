from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.items.item_categories import ItemCategory
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


class ItemPocket(CommonResource):
    categories: List["NamedAPIResource[ItemCategory]"]
    names: List["Name"]

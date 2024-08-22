from typing import List
from aiopoke.models.items.item_categories import ItemCategory
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Name,
)


class ItemPocket(CommonResource):
    categories: List[NamedAPIResource[ItemCategory]]
    names: List[Name]

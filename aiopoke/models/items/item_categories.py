from typing import List
from aiopoke.models.items.item import Item
from aiopoke.models.items.item_pockets import ItemPocket
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Name,
)


class ItemCategory(CommonResource):
    items: List[AdditionalResource[Item]]
    names: List[Name]
    pocket: AdditionalResource[ItemPocket]

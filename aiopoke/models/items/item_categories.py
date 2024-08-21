from typing import List
from aiopoke.models.items.item_pockets import ItemPocket
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


class ItemCategory(CommonResource):
    items: List[AdditionalResource]
    names: List[Name]
    pocket: AdditionalResource

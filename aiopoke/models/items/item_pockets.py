from typing import List
from aiopoke.models.items.item_categories import ItemCategory
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


class ItemPocket(CommonResource):
    categories: List[AdditionalResource]
    names: List[Name]

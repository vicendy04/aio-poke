from dataclasses import dataclass
from typing import List

from aiopoke.models.items.item import Item
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Description,
    Name,
)


@dataclass
class ItemAttribute(CommonResource):
    descriptions: List[Description]
    items: List[NamedAPIResource["Item"]]
    names: List[Name]

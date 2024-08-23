from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Description,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.items.item import Item


@dataclass
class ItemAttribute(CommonResource):
    descriptions: List["Description"]
    items: List["NamedAPIResource[Item]"]
    names: List["Name"]

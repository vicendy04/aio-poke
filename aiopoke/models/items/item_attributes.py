from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        descriptions: List[Dict[str, Any]],
        items: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.descriptions = (
            [Description(**description) for description in descriptions]
            if descriptions
            else []
        )
        self.items = [NamedAPIResource(**item) for item in items] if items else []
        self.names = [Name(**name) for name in names] if names else []

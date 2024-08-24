from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.berries.berries import Berry


@dataclass
class BerryFirmness(CommonResource):
    berries: List["NamedAPIResource[Berry]"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        berries: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.berries = (
            [NamedAPIResource(**berry) for berry in berries] if berries else []
        )
        self.names = [Name(**name) for name in names] if names else []

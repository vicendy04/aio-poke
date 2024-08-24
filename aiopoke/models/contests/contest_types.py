from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import CommonResource, NamedAPIResource
from aiopoke.models.utility.languages import Language

if TYPE_CHECKING:
    from aiopoke.models.berries.berry_flavors import BerryFlavor


@dataclass
class ContestName:
    name: str
    color: str
    language: NamedAPIResource[Language]

    def __init__(
        self,
        *,
        name: str,
        color: str,
        language: Dict[str, Any],
    ) -> None:
        self.name = name
        self.color = color
        self.language = NamedAPIResource(**language)


@dataclass
class ContestType(CommonResource):
    berry_flavor: NamedAPIResource[BerryFlavor]
    names: List["ContestName"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        berry_flavor: Dict[str, Any],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.berry_flavor = NamedAPIResource(**berry_flavor)
        self.names = [ContestName(**name) for name in names] if names else []

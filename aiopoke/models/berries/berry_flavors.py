from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import CommonResource, Name, NamedAPIResource

if TYPE_CHECKING:
    from aiopoke.models.berries.berries import Berry
    from aiopoke.models.contests.contest_types import ContestType


@dataclass
class FlavorBerryMap:
    potency: int
    berry: NamedAPIResource["Berry"]

    def __init__(
        self,
        *,
        potency: int,
        berry: Dict[str, Any],
    ) -> None:
        self.potency = potency
        self.berry = NamedAPIResource(**berry)


@dataclass
class BerryFlavor(CommonResource):
    berries: List["FlavorBerryMap"]
    contest_type: NamedAPIResource["ContestType"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        berries: List[Dict[str, Any]],
        contest_type: Dict[str, Any],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.berries = [FlavorBerryMap(**berry) for berry in berries] if berries else []
        self.contest_type = NamedAPIResource(**contest_type)
        self.names = [Name(**name) for name in names] if names else []

from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import CommonResource, Name, NamedAPIResource

if TYPE_CHECKING:
    from aiopoke.models.berries.berries import Berry
    from aiopoke.models.contests.contest_types import ContestType


@dataclass
class FlavorBerryMap:
    potency: int
    berry: NamedAPIResource["Berry"]


@dataclass
class BerryFlavor(CommonResource):
    berries: List["FlavorBerryMap"]
    contest_type: NamedAPIResource["ContestType"]
    names: List["Name"]

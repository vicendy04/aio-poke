from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import CommonResource, NamedAPIResource
from aiopoke.models.utility.languages import Language

if TYPE_CHECKING:
    from aiopoke.models.berries.berry_flavors import BerryFlavor


@dataclass
class ContestName:
    name: str
    color: str
    language: NamedAPIResource[Language]


@dataclass
class ContestType(CommonResource):
    berry_flavor: NamedAPIResource[BerryFlavor]
    names: List["ContestName"]

from dataclasses import dataclass
from typing import List

from aiopoke.models.berries.berry_flavors import BerryFlavor
from aiopoke.models.utility.common_model import NamedAPIResource, CommonResource
from aiopoke.models.utility.languages import Language


@dataclass
class ContestName:
    name: str
    color: str
    language: NamedAPIResource[Language]


@dataclass
class ContestType(CommonResource):
    berry_flavor: NamedAPIResource[BerryFlavor]
    names: List[ContestName]

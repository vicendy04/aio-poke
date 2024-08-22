from dataclasses import dataclass
from typing import List

from aiopoke.models.berries.berries import Berry
from aiopoke.models.contests.contest_types import ContestType
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Name,
)


@dataclass
class FlavorBerryMap:
    potency: int
    berry: NamedAPIResource[Berry]


@dataclass
class BerryFlavor(CommonResource):
    berries: List[FlavorBerryMap]
    contest_type: NamedAPIResource[ContestType]
    names: List[Name]

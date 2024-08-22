from dataclasses import dataclass
from typing import List

from aiopoke.models.berries.berries import Berry
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Name,
)


@dataclass
class BerryFirmness(CommonResource):
    berries: List[NamedAPIResource[Berry]]
    names: List[Name]

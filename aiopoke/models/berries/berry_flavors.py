from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class FlavorBerryMap:
    potency: int
    berry: AdditionalResource


@dataclass
class BerryFlavor(CommonResource):
    berries: List[FlavorBerryMap]
    contest_type: AdditionalResource
    names: List[Name]

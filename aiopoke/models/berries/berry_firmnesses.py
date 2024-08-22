from dataclasses import dataclass
from typing import List

from aiopoke.models.berries.berries import Berry
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class BerryFirmness(CommonResource):
    berries: List[AdditionalResource[Berry]]
    names: List[Name]

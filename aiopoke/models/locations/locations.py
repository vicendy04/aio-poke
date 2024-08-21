from dataclasses import dataclass
from typing import List


from aiopoke.models.locations.location_areas import LocationArea
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    GenerationGameIndex,
    Name,
)


@dataclass
class Location(CommonResource):
    region: AdditionalResource
    names: List[Name]
    game_indices: List[GenerationGameIndex]
    areas: List[LocationArea]

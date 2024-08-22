from dataclasses import dataclass
from typing import List


from aiopoke.models.locations.location_areas import LocationArea
from aiopoke.models.locations.regions import Region
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    GenerationGameIndex,
    Name,
)


@dataclass
class Location(CommonResource):
    region: NamedAPIResource[Region]
    names: List[Name]
    game_indices: List[GenerationGameIndex]
    areas: List[NamedAPIResource[LocationArea]]

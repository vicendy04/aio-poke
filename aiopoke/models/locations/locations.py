from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    GenerationGameIndex,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.locations.location_areas import LocationArea
    from aiopoke.models.locations.regions import Region


@dataclass
class Location(CommonResource):
    region: NamedAPIResource["Region"]
    names: List["Name"]
    game_indices: List["GenerationGameIndex"]
    areas: List["NamedAPIResource[LocationArea]"]

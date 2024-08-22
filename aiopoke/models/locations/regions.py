from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.games.pokedexs import Pokedex
from aiopoke.models.games.version_groups import VersionGroup
from aiopoke.models.locations.locations import Location
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Name,
)

if TYPE_CHECKING:
    from aiopoke.models.games.generations import Generation


@dataclass
class Region(CommonResource):
    locations: List[AdditionalResource[Location]]
    main_generation: AdditionalResource[Generation]
    names: List[Name]
    pokedexes: List[AdditionalResource[Pokedex]]
    version_groups: List[AdditionalResource[VersionGroup]]

from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.games.generations import Generation
    from aiopoke.models.games.pokedexs import Pokedex
    from aiopoke.models.games.version_groups import VersionGroup
    from aiopoke.models.locations.locations import Location
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


@dataclass
class Region(CommonResource):
    locations: List["NamedAPIResource[Location]"]
    main_generation: NamedAPIResource["Generation"]
    names: List["Name"]
    pokedexes: List["NamedAPIResource[Pokedex]"]
    version_groups: List["NamedAPIResource[VersionGroup]"]

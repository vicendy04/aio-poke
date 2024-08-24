from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        locations: List[Dict[str, Any]],
        main_generation: Dict[str, Any],
        names: List[Dict[str, Any]],
        pokedexes: List[Dict[str, Any]],
        version_groups: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.locations = (
            [NamedAPIResource(**location) for location in locations]
            if locations
            else []
        )
        self.main_generation = NamedAPIResource(**main_generation)
        self.names = [Name(**name) for name in names] if names else []
        self.pokedexes = (
            [NamedAPIResource(**pokedex) for pokedex in pokedexes] if pokedexes else []
        )
        self.version_groups = (
            [NamedAPIResource(**version_group) for version_group in version_groups]
            if version_groups
            else []
        )

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        region: Dict[str, Any],
        names: List[Dict[str, Any]],
        game_indices: List[Dict[str, Any]],
        areas: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.region = NamedAPIResource(**region)
        self.names = [Name(**name) for name in names] if names else []
        self.game_indices = (
            [GenerationGameIndex(**index) for index in game_indices]
            if game_indices
            else []
        )
        self.areas = [NamedAPIResource(**area) for area in areas] if areas else []

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.games.version_groups import VersionGroup
    from aiopoke.models.locations.regions import Region
    from aiopoke.models.moves.moves import Move
    from aiopoke.models.pokemon.abilities import Ability
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
    from aiopoke.models.pokemon.types import Type


@dataclass
class Generation(CommonResource):
    abilities: List["NamedAPIResource[Ability]"]
    main_region: NamedAPIResource["Region"]
    moves: List["NamedAPIResource[Move]"]
    names: List["Name"]
    pokemon_species: List["NamedAPIResource[PokemonSpecies]"]
    types: List["NamedAPIResource[Type]"]
    version_groups: List["NamedAPIResource[VersionGroup]"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        abilities: List[Dict[str, Any]],
        main_region: Dict[str, Any],
        moves: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        pokemon_species: List[Dict[str, Any]],
        types: List[Dict[str, Any]],
        version_groups: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.abilities = (
            [NamedAPIResource(**ability) for ability in abilities] if abilities else []
        )
        self.main_region = NamedAPIResource(**main_region)
        self.moves = [NamedAPIResource(**move) for move in moves] if moves else []
        self.names = [Name(**name) for name in names] if names else []
        self.pokemon_species = (
            [NamedAPIResource(**species) for species in pokemon_species]
            if pokemon_species
            else []
        )
        self.types = [NamedAPIResource(**type_) for type_ in types] if types else []
        self.version_groups = (
            [NamedAPIResource(**version_group) for version_group in version_groups]
            if version_groups
            else []
        )

from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Description,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.games.version_groups import VersionGroup
    from aiopoke.models.locations.regions import Region
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies


@dataclass
class PokemonEntry:
    entry_number: int
    pokemon_species: NamedAPIResource["PokemonSpecies"]

    def __init__(
        self,
        *,
        entry_number: int,
        pokemon_species: Dict[str, Any],
    ) -> None:
        self.entry_number = entry_number
        self.pokemon_species = NamedAPIResource(**pokemon_species)


@dataclass
class Pokedex(CommonResource):
    is_main_series: bool
    descriptions: List["Description"]
    names: List["Name"]
    pokemon_entries: List["PokemonEntry"]
    region: NamedAPIResource["Region"]
    version_groups: List[NamedAPIResource["VersionGroup"]]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        is_main_series: bool,
        descriptions: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        pokemon_entries: List[Dict[str, Any]],
        region: Dict[str, Any],
        version_groups: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.is_main_series = is_main_series
        self.descriptions = (
            [Description(**description) for description in descriptions]
            if descriptions
            else []
        )
        self.names = [Name(**name) for name in names] if names else []
        self.pokemon_entries = (
            [PokemonEntry(**entry) for entry in pokemon_entries]
            if pokemon_entries
            else []
        )
        self.region = NamedAPIResource(**region)
        self.version_groups = (
            [NamedAPIResource(**version_group) for version_group in version_groups]
            if version_groups
            else []
        )

from dataclasses import dataclass
from typing import List

from aiopoke.models.games.version_groups import VersionGroup
from aiopoke.models.locations.regions import Region
from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Description,
    Name,
)


@dataclass
class PokemonEntry:
    entry_number: int
    pokemon_species: NamedAPIResource[PokemonSpecies]


@dataclass
class Pokedex(CommonResource):
    is_main_series: bool
    descriptions: List[Description]
    names: List[Name]
    pokemon_entries: List[PokemonEntry]
    region: NamedAPIResource[Region]
    version_groups: List[NamedAPIResource[VersionGroup]]

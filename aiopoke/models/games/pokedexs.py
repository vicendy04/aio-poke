from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Description,
    Name,
)


@dataclass
class Region:
    name: str
    url: str


@dataclass
class PokemonEntry:
    entry_number: int
    pokemon_species: AdditionalResource


@dataclass
class Pokedex(CommonResource):
    is_main_series: bool
    descriptions: List[Description]
    names: List[Name]
    pokemon_entries: List[PokemonEntry]
    region: AdditionalResource
    version_groups: List[AdditionalResource]

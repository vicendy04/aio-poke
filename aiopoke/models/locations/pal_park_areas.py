from dataclasses import dataclass
from typing import List
from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Name,
)


@dataclass
class PalParkEncounterSpecies:
    base_score: int
    rate: int
    pokemon_species: NamedAPIResource[PokemonSpecies]


@dataclass
class PalParkArea(CommonResource):
    pokemon_encounters: List["PalParkEncounterSpecies"]
    names: List["Name"]

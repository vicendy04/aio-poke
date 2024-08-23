from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


@dataclass
class PalParkEncounterSpecies:
    base_score: int
    rate: int
    pokemon_species: NamedAPIResource["PokemonSpecies"]


@dataclass
class PalParkArea(CommonResource):
    pokemon_encounters: List["PalParkEncounterSpecies"]
    names: List["Name"]

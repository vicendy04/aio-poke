from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    CommonResource,
    Description,
    NamedAPIResource,
)


@dataclass
class GrowthRateExperienceLevel:
    level: int
    experience: int


@dataclass
class GrowthRate(CommonResource):
    descriptions: List["Description"]
    formula: str
    levels: List["GrowthRateExperienceLevel"]
    pokemon_species: List["NamedAPIResource[PokemonSpecies]"]

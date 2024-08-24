from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        descriptions: List[Dict[str, Any]],
        formula: str,
        levels: List[Dict[str, Any]],
        pokemon_species: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.descriptions = (
            [Description(**description) for description in descriptions]
            if descriptions
            else []
        )
        self.formula = formula
        self.levels = (
            [GrowthRateExperienceLevel(**level) for level in levels] if levels else []
        )
        self.pokemon_species = (
            [NamedAPIResource(**species) for species in pokemon_species]
            if pokemon_species
            else []
        )

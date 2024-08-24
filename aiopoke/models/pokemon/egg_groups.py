from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


@dataclass
class EggGroup(CommonResource):
    pokemon_species: List["NamedAPIResource[PokemonSpecies]"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        pokemon_species: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.pokemon_species = (
            [NamedAPIResource(**species) for species in pokemon_species]
            if pokemon_species
            else []
        )
        self.names = [Name(**name) for name in names] if names else []

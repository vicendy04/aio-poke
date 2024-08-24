from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


class PokemonColor(CommonResource):
    names: List["Name"]
    pokemon_species: List["NamedAPIResource[PokemonSpecies]"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        names: List[Dict[str, Any]],
        pokemon_species: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.names = [Name(**name) for name in names] if names else []
        self.pokemon_species = (
            [NamedAPIResource(**species) for species in pokemon_species]
            if pokemon_species
            else []
        )

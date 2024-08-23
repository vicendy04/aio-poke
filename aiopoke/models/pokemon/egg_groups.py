from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


class EggGroup(CommonResource):
    pokemon_species: List["NamedAPIResource[PokemonSpecies]"]
    names: List["Name"]

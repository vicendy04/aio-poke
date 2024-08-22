from typing import List
from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Name,
)


class EggGroup(CommonResource):
    pokemon_species: List[AdditionalResource[PokemonSpecies]]
    names: List[Name]

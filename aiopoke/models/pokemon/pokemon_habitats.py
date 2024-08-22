from typing import List
from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Name,
)


class PokemonHabitat(CommonResource):
    names: List[Name]
    pokemon_species: List[NamedAPIResource[PokemonSpecies]]

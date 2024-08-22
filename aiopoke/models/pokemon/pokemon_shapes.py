from typing import List
from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Name,
)
from aiopoke.models.utility.languages import Language


class AwesomeName:
    awesome_name: str
    language: NamedAPIResource[Language]


class PokemonShape(CommonResource):
    awesome_names: List[AwesomeName]
    names: List[Name]
    pokemon_species: List[NamedAPIResource[PokemonSpecies]]

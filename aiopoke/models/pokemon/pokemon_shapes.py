from typing import List
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


class AwesomeName:
    awesome_name: str
    language: AdditionalResource


class PokemonShape(CommonResource):
    awesome_names: List[AwesomeName]
    names: List[Name]
    pokemon_species: List[AdditionalResource]

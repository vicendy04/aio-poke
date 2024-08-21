from typing import List
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


class PokemonHabitat(CommonResource):
    names: List[Name]
    pokemon_species: List[AdditionalResource]

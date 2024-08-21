from typing import List
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


class EggGroup(CommonResource):
    pokemon_species: List[AdditionalResource]
    names: List[Name]

from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class Generation(CommonResource):
    abilities: List[AdditionalResource]
    main_region: AdditionalResource
    moves: List[AdditionalResource]
    names: List[Name]
    pokemon_species: List[AdditionalResource]
    types: List[AdditionalResource]
    version_groups: List[AdditionalResource]

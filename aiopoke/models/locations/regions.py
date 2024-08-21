from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class Region(CommonResource):
    locations: List[AdditionalResource]
    main_generation: AdditionalResource
    names: List[Name]
    pokedexes: List[AdditionalResource]
    version_groups: List[AdditionalResource]

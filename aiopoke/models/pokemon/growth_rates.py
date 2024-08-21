from dataclasses import dataclass
from typing import List
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Description,
)


@dataclass
class GrowthRateExperienceLevel:
    level: int
    experience: int


@dataclass
class GrowthRate(CommonResource):
    descriptions: List[Description]
    formula: str
    levels: List[GrowthRateExperienceLevel]
    pokemon_species: List[AdditionalResource]

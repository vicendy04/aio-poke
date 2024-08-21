from dataclasses import dataclass
from typing import List
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class NaturePokeathlonStatAffect:
    max_change: int
    nature: AdditionalResource


@dataclass
class NaturePokeathlonStatAffectSets:
    increase: List["NaturePokeathlonStatAffect"]
    decrease: List["NaturePokeathlonStatAffect"]


@dataclass
class PokeathlonStat(CommonResource):
    affecting_natures: NaturePokeathlonStatAffectSets
    names: List[Name]

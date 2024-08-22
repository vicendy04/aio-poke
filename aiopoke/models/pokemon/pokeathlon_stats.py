from dataclasses import dataclass
from typing import List
from aiopoke.models.pokemon.natures import Nature
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Name,
)


@dataclass
class NaturePokeathlonStatAffect:
    max_change: int
    nature: NamedAPIResource[Nature]


@dataclass
class NaturePokeathlonStatAffectSets:
    increase: List["NaturePokeathlonStatAffect"]
    decrease: List["NaturePokeathlonStatAffect"]


@dataclass
class PokeathlonStat(CommonResource):
    affecting_natures: NaturePokeathlonStatAffectSets
    names: List[Name]

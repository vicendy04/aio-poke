from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.natures import Nature
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


@dataclass
class NaturePokeathlonStatAffect:
    max_change: int
    nature: NamedAPIResource["Nature"]


@dataclass
class NaturePokeathlonStatAffectSets:
    increase: List["NaturePokeathlonStatAffect"]
    decrease: List["NaturePokeathlonStatAffect"]


@dataclass
class PokeathlonStat(CommonResource):
    affecting_natures: NaturePokeathlonStatAffectSets
    names: List["Name"]

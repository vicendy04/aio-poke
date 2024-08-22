from dataclasses import dataclass
from typing import List

from aiopoke.models.moves.move_damage_classes import MoveDamageClass
from aiopoke.models.moves.moves import Move
from aiopoke.models.pokemon.natures import Nature
from aiopoke.models.utility.common_model import (
    Resource,
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class MoveStatAffect:
    change: int
    move: AdditionalResource[Move]


@dataclass
class MoveStatAffectSets:
    increase: List[MoveStatAffect]
    decrease: List[MoveStatAffect]


@dataclass
class NatureStatAffectSets:
    increase: List[AdditionalResource[Nature]]
    decrease: List[AdditionalResource[Nature]]


@dataclass
class Stat(CommonResource):
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    # here
    characteristics: List[Resource]
    move_damage_class: AdditionalResource[MoveDamageClass]
    names: List[Name]

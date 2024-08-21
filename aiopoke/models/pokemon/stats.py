from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    APIResource,
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class MoveStatAffect:
    change: int
    move: AdditionalResource


@dataclass
class MoveStatAffectSets:
    increase: List[MoveStatAffect]
    decrease: List[MoveStatAffect]


@dataclass
class NatureStatAffectSets:
    increase: List[AdditionalResource]  # nature
    decrease: List[AdditionalResource]


@dataclass
class Stat(CommonResource):
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: List[APIResource]
    move_damage_class: AdditionalResource
    names: List[Name]

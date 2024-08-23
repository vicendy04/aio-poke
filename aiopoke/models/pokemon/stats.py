from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.moves.move_damage_classes import MoveDamageClass
    from aiopoke.models.moves.moves import Move
    from aiopoke.models.pokemon.characteristic import Characteristic
    from aiopoke.models.pokemon.natures import Nature
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
    UnnamedAPIResource,
)


@dataclass
class MoveStatAffect:
    change: int
    move: NamedAPIResource["Move"]


@dataclass
class MoveStatAffectSets:
    increase: List["MoveStatAffect"]
    decrease: List["MoveStatAffect"]


@dataclass
class NatureStatAffectSets:
    increase: List[NamedAPIResource["Nature"]]
    decrease: List[NamedAPIResource["Nature"]]


@dataclass
class Stat(CommonResource):
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: List[UnnamedAPIResource["Characteristic"]]
    move_damage_class: NamedAPIResource["MoveDamageClass"]
    names: List["Name"]

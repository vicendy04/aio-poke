from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        change: int,
        move: Dict[str, Any],
    ) -> None:
        self.change = change
        self.move = NamedAPIResource(**move)


@dataclass
class MoveStatAffectSets:
    increase: List["MoveStatAffect"]
    decrease: List["MoveStatAffect"]

    def __init__(
        self,
        *,
        increase: List[Dict[str, Any]],
        decrease: List[Dict[str, Any]],
    ) -> None:
        self.increase = (
            [MoveStatAffect(**affect) for affect in increase] if increase else []
        )
        self.decrease = (
            [MoveStatAffect(**affect) for affect in decrease] if decrease else []
        )


@dataclass
class NatureStatAffectSets:
    increase: List[NamedAPIResource["Nature"]]
    decrease: List[NamedAPIResource["Nature"]]

    def __init__(
        self,
        *,
        increase: List[Dict[str, Any]],
        decrease: List[Dict[str, Any]],
    ) -> None:
        self.increase = (
            [NamedAPIResource(**nature) for nature in increase] if increase else []
        )
        self.decrease = (
            [NamedAPIResource(**nature) for nature in decrease] if decrease else []
        )


@dataclass
class Stat(CommonResource):
    game_index: int
    is_battle_only: bool
    affecting_moves: MoveStatAffectSets
    affecting_natures: NatureStatAffectSets
    characteristics: List[UnnamedAPIResource["Characteristic"]]
    move_damage_class: NamedAPIResource["MoveDamageClass"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        game_index: int,
        is_battle_only: bool,
        affecting_moves: Dict[str, Any],
        affecting_natures: Dict[str, Any],
        characteristics: List[Dict[str, Any]],
        move_damage_class: Dict[str, Any],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.game_index = game_index
        self.is_battle_only = is_battle_only
        self.affecting_moves = MoveStatAffectSets(**affecting_moves)
        self.affecting_natures = NatureStatAffectSets(**affecting_natures)
        self.characteristics = (
            [UnnamedAPIResource(**characteristic) for characteristic in characteristics]
            if characteristics
            else []
        )
        self.move_damage_class = NamedAPIResource(**move_damage_class)
        self.names = [Name(**name) for name in names] if names else []

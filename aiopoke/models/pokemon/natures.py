from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.berries.berry_flavors import BerryFlavor
    from aiopoke.models.moves.move_battle_styles import MoveBatteStyle
    from aiopoke.models.pokemon.pokeathlon_stats import PokeathlonStat
    from aiopoke.models.pokemon.stats import Stat
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


@dataclass
class MoveBattleStylePreference:
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: NamedAPIResource["MoveBatteStyle"]

    def __init__(
        self,
        *,
        low_hp_preference: int,
        high_hp_preference: int,
        move_battle_style: Dict[str, Any],
    ) -> None:
        self.low_hp_preference = low_hp_preference
        self.high_hp_preference = high_hp_preference
        self.move_battle_style = NamedAPIResource(**move_battle_style)


@dataclass
class NatureStatChange:
    max_change: int
    pokeathlon_stat: NamedAPIResource["PokeathlonStat"]

    def __init__(
        self,
        *,
        max_change: int,
        pokeathlon_stat: Dict[str, Any],
    ) -> None:
        self.max_change = max_change
        self.pokeathlon_stat = NamedAPIResource(**pokeathlon_stat)


@dataclass
class Nature(CommonResource):
    decreased_stat: NamedAPIResource["Stat"]
    increased_stat: NamedAPIResource["Stat"]
    likes_flavor: NamedAPIResource["BerryFlavor"]
    hates_flavor: NamedAPIResource["BerryFlavor"]
    pokeathlon_stat_changes: List["NatureStatChange"]
    move_battle_style_preferences: List["MoveBattleStylePreference"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        decreased_stat: Dict[str, Any],
        increased_stat: Dict[str, Any],
        likes_flavor: Dict[str, Any],
        hates_flavor: Dict[str, Any],
        pokeathlon_stat_changes: List[Dict[str, Any]],
        move_battle_style_preferences: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.decreased_stat = NamedAPIResource(**decreased_stat)
        self.increased_stat = NamedAPIResource(**increased_stat)
        self.likes_flavor = NamedAPIResource(**likes_flavor)
        self.hates_flavor = NamedAPIResource(**hates_flavor)
        self.pokeathlon_stat_changes = (
            [NatureStatChange(**stat_change) for stat_change in pokeathlon_stat_changes]
            if pokeathlon_stat_changes
            else []
        )
        self.move_battle_style_preferences = (
            [
                MoveBattleStylePreference(**preference)
                for preference in move_battle_style_preferences
            ]
            if move_battle_style_preferences
            else []
        )
        self.names = [Name(**name) for name in names] if names else []

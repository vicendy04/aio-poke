from dataclasses import dataclass
from typing import TYPE_CHECKING, List

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


@dataclass
class NatureStatChange:
    max_change: int
    pokeathlon_stat: NamedAPIResource["PokeathlonStat"]


@dataclass
class Nature(CommonResource):
    decreased_stat: NamedAPIResource["Stat"]
    increased_stat: NamedAPIResource["Stat"]
    likes_flavor: NamedAPIResource["BerryFlavor"]
    hates_flavor: NamedAPIResource["BerryFlavor"]
    pokeathlon_stat_changes: List["NatureStatChange"]
    move_battle_style_preferences: List["MoveBattleStylePreference"]
    names: List["Name"]

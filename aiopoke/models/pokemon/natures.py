from dataclasses import dataclass
from typing import List

from aiopoke.models.berries.berry_flavors import BerryFlavor
from aiopoke.models.moves.move_battle_styles import MoveBatteStyle
from aiopoke.models.pokemon.pokeathlon_stats import PokeathlonStat
from aiopoke.models.pokemon.stats import Stat
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class MoveBattleStylePreference:
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: AdditionalResource[MoveBatteStyle]


@dataclass
class NatureStatChange:
    max_change: int
    pokeathlon_stat: AdditionalResource[PokeathlonStat]


@dataclass
class Nature(CommonResource):
    decreased_stat: AdditionalResource[Stat]
    increased_stat: AdditionalResource[Stat]

    likes_flavor: AdditionalResource[BerryFlavor]
    hates_flavor: AdditionalResource[BerryFlavor]
    pokeathlon_stat_changes: List[NatureStatChange]
    move_battle_style_preferences: List[MoveBattleStylePreference]
    names: List[Name]

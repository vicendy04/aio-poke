from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import CommonResource


@dataclass
class AdditionalResource:
    name: str
    url: str


@dataclass
class MoveBattleStylePreference:
    low_hp_preference: int
    high_hp_preference: int
    move_battle_style: AdditionalResource


@dataclass
class Name:
    name: str
    language: AdditionalResource


@dataclass
class NatureStatChange:
    max_change: int
    pokeathlon_stat: AdditionalResource


@dataclass
class Nature(CommonResource):
    decreased_stat: AdditionalResource
    increased_stat: AdditionalResource

    likes_flavor: AdditionalResource
    hates_flavor: AdditionalResource
    pokeathlon_stat_changes: List[NatureStatChange]
    move_battle_style_preferences: List[MoveBattleStylePreference]
    names: List[Name]

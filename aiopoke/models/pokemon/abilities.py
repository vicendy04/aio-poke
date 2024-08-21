from dataclasses import dataclass
from typing import List

from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Effect,
    Name,
    VerboseEffect,
)


@dataclass
class AbilityEffectChange:
    version_group: AdditionalResource
    effect_entries: List[Effect]


@dataclass
class AbilityFlavorText:
    flavor_text: str
    language: AdditionalResource
    version_group: AdditionalResource


@dataclass
class Ability(CommonResource):
    is_main_series: bool
    generation: AdditionalResource
    names: List[Name]
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    flavor_text_entries: List[AbilityFlavorText]
    pokemon: List[Pokemon]

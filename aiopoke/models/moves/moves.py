from dataclasses import dataclass
from typing import List
from aiopoke.models.contests.super_contest_effects import SuperContestEffect
from aiopoke.models.moves.move_ailments import MoveAilment
from aiopoke.models.pokemon.abilities import AbilityEffectChange
from aiopoke.models.utility.common_models import (
    APIResource,
    AdditionalResource,
    CommonResource,
    MachineVersionDetail,
    Name,
    VerboseEffect,
)


@dataclass
class MoveFlavorText:
    flavor_text: str
    language: AdditionalResource
    version_group: AdditionalResource


@dataclass
class MoveMetaData:
    ailment: AdditionalResource
    category: AdditionalResource
    min_hits: int
    max_hits: int
    min_turns: int
    max_turns: int
    drain: int
    healing: int
    crit_rate: int
    ailment_chance: int
    flinch_chance: int
    stat_chance: int


class PastMoveStatValues:
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entries: List[VerboseEffect]
    type: AdditionalResource
    version_group: AdditionalResource


@dataclass
class MoveStatChange:
    change: int
    stat: AdditionalResource


class Move(CommonResource):
    accuracy: int
    effect_chance: int
    pp: int
    priority: int
    power: int
    contest_combos: AdditionalResource
    contest_type: AdditionalResource
    contest_effect: APIResource
    damage_class: AdditionalResource
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    machines: List[MachineVersionDetail]
    generation: AdditionalResource
    meta: MoveMetaData
    names: List[Name]
    past_values: List[PastMoveStatValues]
    stat_changes: List[MoveStatChange]
    super_contest_effect: APIResource
    target: AdditionalResource
    type: AdditionalResource
    learned_by_pokemon: List[AdditionalResource]
    flavor_text_entries: List[MoveFlavorText]

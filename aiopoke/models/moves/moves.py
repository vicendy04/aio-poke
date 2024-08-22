from dataclasses import dataclass
from typing import List, Optional

from aiopoke.models.contests.contest_types import ContestType
from aiopoke.models.contests.super_contest_effects import SuperContestEffect
from aiopoke.models.games.generations import Generation
from aiopoke.models.games.version_groups import VersionGroup
from aiopoke.models.moves.move_ailments import MoveAilment
from aiopoke.models.moves.move_categories import MoveCategory
from aiopoke.models.moves.move_damage_classes import MoveDamageClass
from aiopoke.models.moves.move_targets import MoveTarget
from aiopoke.models.pokemon.abilities import AbilityEffectChange
from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.pokemon.stats import Stat
from aiopoke.models.pokemon.types import Type
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    MachineVersionDetail,
    Name,
    Resource,
    VerboseEffect,
)
from aiopoke.models.utility.languages import Language


@dataclass
class MoveFlavorText:
    flavor_text: str
    language: AdditionalResource[Language]
    version_group: AdditionalResource[VersionGroup]


@dataclass
class MoveMetaData:
    ailment: AdditionalResource[MoveAilment]
    category: AdditionalResource[MoveCategory]
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
    type: AdditionalResource[Type]
    version_group: AdditionalResource[VersionGroup]


@dataclass
class MoveStatChange:
    change: int
    stat: AdditionalResource[Stat]


class ContestComboDetail:
    use_before: Optional[List[AdditionalResource["Move"]]]
    use_after: Optional[List[AdditionalResource["Move"]]]


@dataclass
class ContestComboSets:
    normal: ContestComboDetail
    super: ContestComboDetail


class Move(CommonResource):
    accuracy: int
    effect_chance: int
    pp: int
    priority: int
    power: int
    contest_combos: ContestComboSets
    contest_type: AdditionalResource[ContestType]
    # here
    contest_effect: Resource
    damage_class: AdditionalResource[MoveDamageClass]
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    machines: List[MachineVersionDetail]
    generation: AdditionalResource[Generation]
    meta: MoveMetaData
    names: List[Name]
    past_values: List[PastMoveStatValues]
    stat_changes: List[MoveStatChange]
    # here
    super_contest_effect: Resource
    target: AdditionalResource[MoveTarget]
    type: AdditionalResource[Type]
    learned_by_pokemon: List[AdditionalResource[Pokemon]]
    flavor_text_entries: List[MoveFlavorText]

from dataclasses import dataclass
from typing import List, Optional

from aiopoke.models.contests.contest_effects import ContestEffect
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
    NamedAPIResource,
    CommonResource,
    MachineVersionDetail,
    Name,
    UnnamedAPIResource,
    VerboseEffect,
)
from aiopoke.models.utility.languages import Language


@dataclass
class MoveFlavorText:
    flavor_text: str
    language: NamedAPIResource[Language]
    version_group: NamedAPIResource[VersionGroup]


@dataclass
class MoveMetaData:
    ailment: NamedAPIResource[MoveAilment]
    category: NamedAPIResource[MoveCategory]
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
    type: NamedAPIResource[Type]
    version_group: NamedAPIResource[VersionGroup]


@dataclass
class MoveStatChange:
    change: int
    stat: NamedAPIResource[Stat]


class ContestComboDetail:
    use_before: Optional[List[NamedAPIResource["Move"]]]
    use_after: Optional[List[NamedAPIResource["Move"]]]


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
    contest_type: NamedAPIResource[ContestType]
    contest_effect: UnnamedAPIResource[ContestEffect]
    damage_class: NamedAPIResource[MoveDamageClass]
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    machines: List[MachineVersionDetail]
    generation: NamedAPIResource[Generation]
    meta: MoveMetaData
    names: List[Name]
    past_values: List[PastMoveStatValues]
    stat_changes: List[MoveStatChange]
    super_contest_effect: UnnamedAPIResource[SuperContestEffect]
    target: NamedAPIResource[MoveTarget]
    type: NamedAPIResource[Type]
    learned_by_pokemon: List[NamedAPIResource[Pokemon]]
    flavor_text_entries: List[MoveFlavorText]

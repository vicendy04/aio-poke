from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

from aiopoke.models.utility.common_model import (
    CommonResource,
    MachineVersionDetail,
    Name,
    NamedAPIResource,
    UnnamedAPIResource,
    VerboseEffect,
)
from aiopoke.models.utility.languages import Language

if TYPE_CHECKING:
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


@dataclass
class MoveFlavorText:
    flavor_text: str
    language: NamedAPIResource[Language]
    version_group: NamedAPIResource[VersionGroup]


@dataclass
class MoveMetaData:
    ailment: NamedAPIResource[MoveAilment]
    category: NamedAPIResource[MoveCategory]
    min_hits: Optional[int]
    max_hits: Optional[int]
    min_turns: Optional[int]
    max_turns: Optional[int]
    drain: Optional[int]
    healing: Optional[int]
    crit_rate: Optional[int]
    ailment_chance: Optional[int]
    flinch_chance: Optional[int]
    stat_chance: Optional[int]


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


@dataclass
class ContestComboDetail:
    use_before: Optional[List[NamedAPIResource["Move"]]]
    use_after: Optional[List[NamedAPIResource["Move"]]]


@dataclass
class ContestComboSets:
    normal: ContestComboDetail
    super: ContestComboDetail


@dataclass
class Move(CommonResource):
    accuracy: Optional[int]
    effect_chance: Optional[int]
    pp: Optional[int]
    priority: Optional[int]
    power: Optional[int]
    contest_combos: Optional[ContestComboSets]
    contest_type: Optional[NamedAPIResource[ContestType]]
    contest_effect: Optional[UnnamedAPIResource[ContestEffect]]
    damage_class: Optional[NamedAPIResource[MoveDamageClass]]
    effect_entries: List[VerboseEffect]
    effect_changes: List[AbilityEffectChange]
    machines: List[MachineVersionDetail]
    generation: NamedAPIResource[Generation]
    meta: Optional[MoveMetaData]
    names: List[Name]
    past_values: List[PastMoveStatValues]
    stat_changes: List[MoveStatChange]
    super_contest_effect: Optional[UnnamedAPIResource[SuperContestEffect]]
    target: NamedAPIResource[MoveTarget]
    type: NamedAPIResource[Type]
    learned_by_pokemon: List[NamedAPIResource[Pokemon]]
    flavor_text_entries: List[MoveFlavorText]

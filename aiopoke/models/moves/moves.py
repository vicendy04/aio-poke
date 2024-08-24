from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional

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

    def __init__(
        self,
        *,
        flavor_text: str,
        language: Dict[str, Any],
        version_group: Dict[str, Any],
    ) -> None:
        self.flavor_text = flavor_text
        self.language = NamedAPIResource(**language)
        self.version_group = NamedAPIResource(**version_group)


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

    def __init__(
        self,
        *,
        ailment: Dict[str, Any],
        category: Dict[str, Any],
        min_hits: Optional[int] = None,
        max_hits: Optional[int] = None,
        min_turns: Optional[int] = None,
        max_turns: Optional[int] = None,
        drain: Optional[int] = None,
        healing: Optional[int] = None,
        crit_rate: Optional[int] = None,
        ailment_chance: Optional[int] = None,
        flinch_chance: Optional[int] = None,
        stat_chance: Optional[int] = None,
    ) -> None:
        self.ailment = NamedAPIResource(**ailment)
        self.category = NamedAPIResource(**category)
        self.min_hits = min_hits
        self.max_hits = max_hits
        self.min_turns = min_turns
        self.max_turns = max_turns
        self.drain = drain
        self.healing = healing
        self.crit_rate = crit_rate
        self.ailment_chance = ailment_chance
        self.flinch_chance = flinch_chance
        self.stat_chance = stat_chance


class PastMoveStatValues:
    accuracy: int
    effect_chance: int
    power: int
    pp: int
    effect_entries: List[VerboseEffect]
    type: NamedAPIResource[Type]
    version_group: NamedAPIResource[VersionGroup]

    def __init__(
        self,
        *,
        accuracy: int,
        effect_chance: int,
        power: int,
        pp: int,
        effect_entries: List[Dict[str, Any]],
        type: Dict[str, Any],
        version_group: Dict[str, Any],
    ) -> None:
        self.accuracy = accuracy
        self.effect_chance = effect_chance
        self.power = power
        self.pp = pp
        self.effect_entries = (
            [VerboseEffect(**effect) for effect in effect_entries]
            if effect_entries
            else []
        )
        self.type = NamedAPIResource(**type)
        self.version_group = NamedAPIResource(**version_group)


@dataclass
class MoveStatChange:
    change: int
    stat: NamedAPIResource[Stat]

    def __init__(
        self,
        *,
        change: int,
        stat: Dict[str, Any],
    ) -> None:
        self.change = change
        self.stat = NamedAPIResource(**stat)


@dataclass
class ContestComboDetail:
    use_before: Optional[List[NamedAPIResource["Move"]]]
    use_after: Optional[List[NamedAPIResource["Move"]]]

    def __init__(
        self,
        *,
        use_before: Optional[List[Dict[str, Any]]] = None,
        use_after: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        self.use_before = (
            [NamedAPIResource(**move) for move in use_before] if use_before else []
        )
        self.use_after = (
            [NamedAPIResource(**move) for move in use_after] if use_after else []
        )


@dataclass
class ContestComboSets:
    normal: ContestComboDetail
    super: ContestComboDetail

    def __init__(
        self,
        *,
        normal: Dict[str, Any],
        super: Dict[str, Any],
    ) -> None:
        self.normal = ContestComboDetail(**normal)
        self.super = ContestComboDetail(**super)


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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        accuracy: Optional[int] = None,
        effect_chance: Optional[int] = None,
        pp: Optional[int] = None,
        priority: Optional[int] = None,
        power: Optional[int] = None,
        contest_combos: Optional[Dict[str, Any]] = None,
        contest_type: Optional[Dict[str, Any]] = None,
        contest_effect: Optional[Dict[str, Any]] = None,
        damage_class: Optional[Dict[str, Any]] = None,
        effect_entries: List[Dict[str, Any]],
        effect_changes: List[Dict[str, Any]],
        machines: List[Dict[str, Any]],
        generation: Dict[str, Any],
        meta: Optional[Dict[str, Any]] = None,
        names: List[Dict[str, Any]],
        past_values: List[Dict[str, Any]],
        stat_changes: List[Dict[str, Any]],
        super_contest_effect: Optional[Dict[str, Any]] = None,
        target: Dict[str, Any],
        type: Dict[str, Any],
        learned_by_pokemon: List[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.accuracy = accuracy
        self.effect_chance = effect_chance
        self.pp = pp
        self.priority = priority
        self.power = power
        self.contest_combos = (
            ContestComboSets(**contest_combos) if contest_combos else None
        )
        self.contest_type = NamedAPIResource(**contest_type) if contest_type else None
        self.contest_effect = (
            UnnamedAPIResource(**contest_effect) if contest_effect else None
        )
        self.damage_class = NamedAPIResource(**damage_class) if damage_class else None
        self.effect_entries = (
            [VerboseEffect(**effect) for effect in effect_entries]
            if effect_entries
            else []
        )
        self.effect_changes = (
            [AbilityEffectChange(**change) for change in effect_changes]
            if effect_changes
            else []
        )
        self.machines = (
            [MachineVersionDetail(**machine) for machine in machines]
            if machines
            else []
        )
        self.generation = NamedAPIResource(**generation)
        self.meta = MoveMetaData(**meta) if meta else None
        self.names = [Name(**name) for name in names] if names else []
        self.past_values = (
            [PastMoveStatValues(**value) for value in past_values]
            if past_values
            else []
        )
        self.stat_changes = (
            [MoveStatChange(**stat_change) for stat_change in stat_changes]
            if stat_changes
            else []
        )
        self.super_contest_effect = (
            UnnamedAPIResource(**super_contest_effect) if super_contest_effect else None
        )
        self.target = NamedAPIResource(**target)
        self.type = NamedAPIResource(**type)
        self.learned_by_pokemon = (
            [NamedAPIResource(**pokemon) for pokemon in learned_by_pokemon]
            if learned_by_pokemon
            else []
        )
        self.flavor_text_entries = (
            [MoveFlavorText(**flavor_text) for flavor_text in flavor_text_entries]
            if flavor_text_entries
            else []
        )

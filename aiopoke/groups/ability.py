from dataclasses import dataclass
from typing import List


@dataclass
class Generation:
    name: str
    url: str


@dataclass
class EffectChangeEffectEntry:
    effect: str
    language: Generation


@dataclass
class EffectChange:
    effect_entries: List[EffectChangeEffectEntry]
    version_group: Generation


@dataclass
class AbilityEffectEntry:
    effect: str
    language: Generation
    short_effect: str


@dataclass
class FlavorTextEntry:
    flavor_text: str
    language: Generation
    version_group: Generation


@dataclass
class Name:
    language: Generation
    name: str


@dataclass
class Pokemon:
    is_hidden: bool
    pokemon: Generation
    slot: int


@dataclass
class Ability:
    effect_changes: List[EffectChange]
    effect_entries: List[AbilityEffectEntry]
    flavor_text_entries: List[FlavorTextEntry]
    generation: Generation
    id: int
    is_main_series: bool
    name: str
    names: List[Name]
    pokemon: List[Pokemon]

from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.games.generations import Generation
    from aiopoke.models.games.version_groups import VersionGroup
    from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.utility.common_model import (
    CommonResource,
    Effect,
    Name,
    NamedAPIResource,
    VerboseEffect,
)
from aiopoke.models.utility.languages import Language


@dataclass
class AbilityEffectChange:
    version_group: "NamedAPIResource[VersionGroup]"
    effect_entries: List["Effect"]


@dataclass
class AbilityFlavorText:
    flavor_text: str
    language: "NamedAPIResource[Language]"
    version_group: "NamedAPIResource[VersionGroup]"


@dataclass
class AbilityPokemon:
    is_hidden: bool
    slot: int
    pokemon: "NamedAPIResource[Pokemon]"


@dataclass
class Ability(CommonResource):
    is_main_series: bool
    generation: "NamedAPIResource[Generation]"
    names: List["Name"]
    effect_entries: List["VerboseEffect"]
    effect_changes: List["AbilityEffectChange"]
    flavor_text_entries: List["AbilityFlavorText"]
    pokemon: List["AbilityPokemon"]

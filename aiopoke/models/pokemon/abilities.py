from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        version_group: Dict[str, Any],
        effect_entries: List[Dict[str, Any]],
    ) -> None:
        self.version_group = NamedAPIResource(**version_group)
        self.effect_entries = (
            [Effect(**effect) for effect in effect_entries] if effect_entries else []
        )


@dataclass
class AbilityFlavorText:
    flavor_text: str
    language: "NamedAPIResource[Language]"
    version_group: "NamedAPIResource[VersionGroup]"

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
class AbilityPokemon:
    is_hidden: bool
    slot: int
    pokemon: "NamedAPIResource[Pokemon]"

    def __init__(
        self,
        *,
        is_hidden: bool,
        slot: int,
        pokemon: Dict[str, Any],
    ) -> None:
        self.is_hidden = is_hidden
        self.slot = slot
        self.pokemon = NamedAPIResource(**pokemon)


@dataclass
class Ability(CommonResource):
    is_main_series: bool
    generation: "NamedAPIResource[Generation]"
    names: List["Name"]
    effect_entries: List["VerboseEffect"]
    effect_changes: List["AbilityEffectChange"]
    flavor_text_entries: List["AbilityFlavorText"]
    pokemon: List["AbilityPokemon"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        is_main_series: bool,
        generation: Dict[str, Any],
        names: List[Dict[str, Any]],
        effect_entries: List[Dict[str, Any]],
        effect_changes: List[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
        pokemon: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.is_main_series = is_main_series
        self.generation = NamedAPIResource(**generation)
        self.names = [Name(**name) for name in names] if names else []
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
        self.flavor_text_entries = (
            [AbilityFlavorText(**flavor_text) for flavor_text in flavor_text_entries]
            if flavor_text_entries
            else []
        )
        self.pokemon = (
            [AbilityPokemon(**pokemon) for pokemon in pokemon] if pokemon else []
        )

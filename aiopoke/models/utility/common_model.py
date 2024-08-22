from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, Generic, List, TypeVar

from aiopoke.models.machines.machines import Machine
from aiopoke.models.utility.languages import Language

if TYPE_CHECKING:
    from aiopoke.models.encounters.encounter_condition_values import (
        EncounterConditionValue,
    )
    from aiopoke.models.encounters.encounter_methods import EncounterMethod
    from aiopoke.models.games.generations import Generation
    from aiopoke.models.games.version import Version
    from aiopoke.models.games.version_groups import VersionGroup


T = TypeVar("T")


@dataclass
class UnnamedAPIResource(Generic[T]):
    url: str


@dataclass
class NamedAPIResource(Generic[T]):
    name: str
    url: str


@dataclass
class Description:
    description: str
    language: NamedAPIResource[Language]


@dataclass
class CommonResource:
    name: str
    id: int


@dataclass
class Name:
    name: str
    language: NamedAPIResource["Language"]

    def __init__(
        self,
        name: str,
        language: Dict[str, Any],
    ):
        self.name = name
        self.language = NamedAPIResource(**language)


@dataclass
class Effect:
    effect: str
    language: NamedAPIResource[Language]


@dataclass
class Encounter:
    min_level: int
    max_level: int
    condition_values: List[NamedAPIResource[EncounterConditionValue]]
    chance: int
    method: NamedAPIResource[EncounterMethod]


@dataclass
class FlavorText:
    flavor_text: str
    language: NamedAPIResource[Language]
    version: NamedAPIResource[Version]


@dataclass
class GenerationGameIndex:
    game_index: int
    generation: NamedAPIResource[Generation]


@dataclass
class MachineVersionDetail:
    machine: UnnamedAPIResource[Machine]
    version_group: NamedAPIResource[VersionGroup]


@dataclass
class VerboseEffect:
    effect: str
    short_effect: str
    language: NamedAPIResource[Language]


@dataclass
class VersionEncounterDetail:
    version: NamedAPIResource[Version]
    max_chance: int
    encounter_details: List[Encounter]


@dataclass
class VersionGameIndex:
    game_index: int
    version: NamedAPIResource[Version]


@dataclass
class VersionGroupFlavorText:
    text: str
    language: NamedAPIResource[Language]
    version_group: NamedAPIResource[VersionGroup]

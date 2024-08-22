from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, Generic, List, TypeVar

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
class Resource:
    url: str


@dataclass
class AdditionalResource(Generic[T]):
    name: str
    url: str


@dataclass
class Description:
    description: str
    language: AdditionalResource[Language]


@dataclass
class CommonResource:
    name: str
    id: int


@dataclass
class Name:
    name: str
    language: AdditionalResource["Language"]

    def __init__(
        self,
        name: str,
        language: Dict[str, Any],
    ):
        self.name = name
        self.language = AdditionalResource(**language)


# here
@dataclass
class Effect:
    effect: str
    language: AdditionalResource[Language]


@dataclass
class Encounter:
    min_level: int
    max_level: int
    condition_values: List[AdditionalResource[EncounterConditionValue]]
    chance: int
    method: AdditionalResource[EncounterMethod]


# here
@dataclass
class FlavorText:
    flavor_text: str
    language: AdditionalResource[Language]
    version: AdditionalResource[Version]


@dataclass
class GenerationGameIndex:
    game_index: int
    generation: AdditionalResource[Generation]


@dataclass
class MachineVersionDetail:
    # here
    machine: Resource
    version_group: AdditionalResource[VersionGroup]


@dataclass
class VerboseEffect:
    effect: str
    short_effect: str
    language: AdditionalResource[Language]


@dataclass
class VersionEncounterDetail:
    version: AdditionalResource[Version]
    max_chance: int
    encounter_details: List[Encounter]


@dataclass
class VersionGameIndex:
    game_index: int
    version: AdditionalResource[Version]


@dataclass
class VersionGroupFlavorText:
    text: str
    language: AdditionalResource[Language]
    version_group: AdditionalResource[VersionGroup]

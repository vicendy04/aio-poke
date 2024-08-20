from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class CommonAPIResource:
    name: str
    id: int


@dataclass
class APIResource:
    url: str


@dataclass
class AdditionalResource:
    name: str
    url: str


@dataclass
class Name:
    name: str
    language: AdditionalResource

    def __init__(
        self,
        name: str,
        language: Dict[str, Any],
    ):
        self.name = name
        self.language = AdditionalResource(**language)


@dataclass
class Description:
    description: str
    language: AdditionalResource


@dataclass
class Effect:
    effect: str
    language: AdditionalResource


@dataclass
class Encounter:
    min_level: int
    max_level: int
    condition_values: List[AdditionalResource]
    chance: int
    method: AdditionalResource


@dataclass
class FlavorText:
    flavor_text: str
    language: AdditionalResource
    version: AdditionalResource


@dataclass
class GameIndeGenerationGameIndex:
    game_index: int
    generation: AdditionalResource


@dataclass
class MachineVersionDetail:
    machine: APIResource
    version_group: AdditionalResource


@dataclass
class VerboseEffect:
    effect: str
    short_effect: str
    language: AdditionalResource


@dataclass
class VersionEncounterDetail:
    version: AdditionalResource
    max_chance: int
    encounter_details: List[Encounter]


@dataclass
class VersionGameIndex:
    game_index: int
    version: AdditionalResource


@dataclass
class VersionGroupFlavorText:
    text: str
    language: AdditionalResource
    version_group: AdditionalResource

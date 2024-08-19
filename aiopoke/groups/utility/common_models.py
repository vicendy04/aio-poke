from dataclasses import dataclass
from typing import List


@dataclass
class IdentifiedResource:
    name: str
    id: int


@dataclass
class NamedAPIResource:
    name: str
    url: str


@dataclass
class Name:
    name: str
    language: NamedAPIResource


@dataclass
class APIResource:
    url: str


@dataclass
class Description:
    description: str
    language: NamedAPIResource


@dataclass
class Effect:
    effect: str
    language: NamedAPIResource


@dataclass
class Encounter:
    min_level: int
    max_level: int
    condition_values: List[NamedAPIResource]
    chance: int
    method: NamedAPIResource


@dataclass
class FlavorText:
    flavor_text: str
    language: NamedAPIResource
    version: NamedAPIResource


@dataclass
class GameIndeGenerationGameIndex:
    game_index: int
    generation: NamedAPIResource


@dataclass
class MachineVersionDetail:
    machine: APIResource
    version_group: NamedAPIResource


@dataclass
class VerboseEffect:
    effect: str
    short_effect: str
    language: NamedAPIResource


@dataclass
class VersionEncounterDetail:
    version: NamedAPIResource
    max_chance: int
    encounter_details: List[Encounter]


@dataclass
class VersionGameIndex:
    game_index: int
    version: NamedAPIResource


@dataclass
class VersionGroupFlavorText:
    text: str
    language: NamedAPIResource
    version_group: NamedAPIResource

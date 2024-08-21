from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
    VersionEncounterDetail,
)


@dataclass
class EncounterVersionDetails:
    rate: int
    version: AdditionalResource


@dataclass
class EncounterMethodRate:
    encounter_method: AdditionalResource
    version_details: List[EncounterVersionDetails]


@dataclass
class PokemonEncounter:
    pokemon: AdditionalResource
    version_details: List[VersionEncounterDetail]


@dataclass
class LocationArea(CommonResource):
    game_index: int
    encounter_method_rates: List[EncounterMethodRate]
    location: AdditionalResource
    names: List[Name]
    pokemon_encounters: List[PokemonEncounter]

from dataclasses import dataclass
from typing import List

from aiopoke.models.encounters.encounter_methods import EncounterMethod
from aiopoke.models.games.version import Version
from aiopoke.models.locations.locations import Location
from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Name,
    VersionEncounterDetail,
)


@dataclass
class EncounterVersionDetails:
    rate: int
    version: NamedAPIResource[Version]


@dataclass
class EncounterMethodRate:
    encounter_method: NamedAPIResource[EncounterMethod]
    version_details: List[EncounterVersionDetails]


@dataclass
class PokemonEncounter:
    pokemon: NamedAPIResource[Pokemon]
    version_details: List[VersionEncounterDetail]


@dataclass
class LocationArea(CommonResource):
    game_index: int
    encounter_method_rates: List[EncounterMethodRate]
    location: NamedAPIResource[Location]
    names: List[Name]
    pokemon_encounters: List[PokemonEncounter]

from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
    VersionEncounterDetail,
)

if TYPE_CHECKING:
    from aiopoke.models.encounters.encounter_methods import EncounterMethod
    from aiopoke.models.games.version import Version
    from aiopoke.models.locations.locations import Location
    from aiopoke.models.pokemon.pokemon import Pokemon


@dataclass
class EncounterVersionDetails:
    rate: int
    version: NamedAPIResource["Version"]


@dataclass
class EncounterMethodRate:
    encounter_method: NamedAPIResource["EncounterMethod"]
    version_details: List["EncounterVersionDetails"]


@dataclass
class PokemonEncounter:
    pokemon: NamedAPIResource["Pokemon"]
    version_details: List["VersionEncounterDetail"]


@dataclass
class LocationArea(CommonResource):
    game_index: int
    encounter_method_rates: List["EncounterMethodRate"]
    location: NamedAPIResource["Location"]
    names: List["Name"]
    pokemon_encounters: List["PokemonEncounter"]

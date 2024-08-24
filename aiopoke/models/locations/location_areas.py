from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        rate: int,
        version: Dict[str, Any],
    ) -> None:
        self.rate = rate
        self.version = NamedAPIResource(**version)


@dataclass
class EncounterMethodRate:
    encounter_method: NamedAPIResource["EncounterMethod"]
    version_details: List["EncounterVersionDetails"]

    def __init__(
        self,
        *,
        encounter_method: Dict[str, Any],
        version_details: List[Dict[str, Any]],
    ) -> None:
        self.encounter_method = NamedAPIResource(**encounter_method)
        self.version_details = (
            [EncounterVersionDetails(**detail) for detail in version_details]
            if version_details
            else []
        )


@dataclass
class PokemonEncounter:
    pokemon: NamedAPIResource["Pokemon"]
    version_details: List["VersionEncounterDetail"]

    def __init__(
        self,
        *,
        pokemon: Dict[str, Any],
        version_details: List[Dict[str, Any]],
    ) -> None:
        self.pokemon = NamedAPIResource(**pokemon)
        self.version_details = (
            [VersionEncounterDetail(**detail) for detail in version_details]
            if version_details
            else []
        )


@dataclass
class LocationArea(CommonResource):
    game_index: int
    encounter_method_rates: List["EncounterMethodRate"]
    location: NamedAPIResource["Location"]
    names: List["Name"]
    pokemon_encounters: List["PokemonEncounter"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        game_index: int,
        encounter_method_rates: List[Dict[str, Any]],
        location: Dict[str, Any],
        names: List[Dict[str, Any]],
        pokemon_encounters: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.game_index = game_index
        self.encounter_method_rates = (
            [EncounterMethodRate(**rate) for rate in encounter_method_rates]
            if encounter_method_rates
            else []
        )
        self.location = NamedAPIResource(**location)
        self.names = [Name(**name) for name in names] if names else []
        self.pokemon_encounters = (
            [PokemonEncounter(**encounter) for encounter in pokemon_encounters]
            if pokemon_encounters
            else []
        )

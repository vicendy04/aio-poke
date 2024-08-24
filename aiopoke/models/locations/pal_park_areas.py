from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


@dataclass
class PalParkEncounterSpecies:
    base_score: int
    rate: int
    pokemon_species: NamedAPIResource["PokemonSpecies"]

    def __init__(
        self,
        *,
        base_score: int,
        rate: int,
        pokemon_species: Dict[str, Any],
    ) -> None:
        self.base_score = base_score
        self.rate = rate
        self.pokemon_species = NamedAPIResource(**pokemon_species)


@dataclass
class PalParkArea(CommonResource):
    pokemon_encounters: List["PalParkEncounterSpecies"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        pokemon_encounters: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.pokemon_encounters = (
            [PalParkEncounterSpecies(**encounter) for encounter in pokemon_encounters]
            if pokemon_encounters
            else []
        )
        self.names = [Name(**name) for name in names] if names else []

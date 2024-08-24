from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)
from aiopoke.models.utility.languages import Language


@dataclass
class AwesomeName:
    awesome_name: str
    language: NamedAPIResource["Language"]

    def __init__(
        self,
        *,
        awesome_name: str,
        language: Dict[str, Any],
    ) -> None:
        self.awesome_name = awesome_name
        self.language = NamedAPIResource(**language)


@dataclass
class PokemonShape(CommonResource):
    awesome_names: List["AwesomeName"]
    names: List["Name"]
    pokemon_species: List["NamedAPIResource[PokemonSpecies]"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        awesome_names: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        pokemon_species: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.awesome_names = (
            [AwesomeName(**awesome_name) for awesome_name in awesome_names]
            if awesome_names
            else []
        )
        self.names = [Name(**name) for name in names] if names else []
        self.pokemon_species = (
            [NamedAPIResource(**species) for species in pokemon_species]
            if pokemon_species
            else []
        )

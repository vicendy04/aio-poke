from dataclasses import dataclass
from typing import List, TYPE_CHECKING

from aiopoke.models.locations.regions import Region
from aiopoke.models.moves.moves import Move
from aiopoke.models.pokemon.abilities import Ability
from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
from aiopoke.models.pokemon.types import Type
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Name,
)

if TYPE_CHECKING:
    from aiopoke.models.games.version_groups import VersionGroup


@dataclass
class Generation(CommonResource):
    abilities: List[AdditionalResource[Ability]]
    main_region: AdditionalResource[Region]
    moves: List[AdditionalResource[Move]]
    names: List[Name]
    pokemon_species: List[AdditionalResource[PokemonSpecies]]
    types: List[AdditionalResource[Type]]
    version_groups: List[AdditionalResource["VersionGroup"]]

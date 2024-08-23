from dataclasses import dataclass
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.games.version_groups import VersionGroup
    from aiopoke.models.pokemon.pokemon import Pokemon, PokemonFormType
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


@dataclass
class PokemonFormSprites:
    back_default: str
    back_female: None
    back_shiny: str
    back_shiny_female: None
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None


@dataclass
class PokemonForm(CommonResource):
    order: int
    form_order: int
    is_default: bool
    is_battle_only: bool
    is_mega: bool
    form_name: str
    pokemon: NamedAPIResource["Pokemon"]
    sprites: PokemonFormSprites
    types: List["PokemonFormType"]
    version_group: NamedAPIResource["VersionGroup"]
    names: List["Name"]
    form_names: List["Name"]

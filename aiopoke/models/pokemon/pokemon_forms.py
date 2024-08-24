from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        order: int,
        form_order: int,
        is_default: bool,
        is_battle_only: bool,
        is_mega: bool,
        form_name: str,
        pokemon: Dict[str, Any],
        sprites: Dict[str, Any],
        types: List[Dict[str, Any]],
        version_group: Dict[str, Any],
        names: List[Dict[str, Any]],
        form_names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.order = order
        self.form_order = form_order
        self.is_default = is_default
        self.is_battle_only = is_battle_only
        self.is_mega = is_mega
        self.form_name = form_name
        self.pokemon = NamedAPIResource(**pokemon)
        self.sprites = PokemonFormSprites(**sprites)
        self.types = [PokemonFormType(**type_) for type_ in types] if types else []
        self.version_group = NamedAPIResource(**version_group)
        self.names = [Name(**name) for name in names] if names else []
        self.form_names = [Name(**name) for name in form_names] if form_names else []

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    NamedAPIResource,
    VersionGameIndex,
)

if TYPE_CHECKING:
    from aiopoke.models.games.generations import Generation
    from aiopoke.models.games.version import Version
    from aiopoke.models.items.item import Item
    from aiopoke.models.moves.move_learn_methods import MoveLearnMethod
    from aiopoke.models.moves.moves import Move
    from aiopoke.models.pokemon.abilities import Ability
    from aiopoke.models.pokemon.pokemon_forms import PokemonForm
    from aiopoke.models.pokemon.pokemon_species import PokemonSpecies
    from aiopoke.models.pokemon.stats import Stat
    from aiopoke.models.pokemon.types import Type


@dataclass
class PokemonFormType:
    slot: int
    type: NamedAPIResource["Type"]

    def __init__(
        self,
        *,
        slot: int,
        type: Dict[str, Any],
    ) -> None:
        self.slot = slot
        self.type = NamedAPIResource(**type)


@dataclass
class PokemonAbility:
    is_hidden: bool
    slot: int
    ability: NamedAPIResource["Ability"]

    def __init__(self, is_hidden: bool, slot: int, ability: Dict[str, Any]):
        self.is_hidden = is_hidden
        self.slot = slot
        self.ability = NamedAPIResource(**ability)


@dataclass
class PokemonCries:
    latest: str
    legacy: str


@dataclass
class PokemonHeldItemVersion:
    rarity: int
    version: NamedAPIResource["Version"]

    def __init__(self, rarity: int, version: Dict[str, Any]):
        self.rarity = rarity
        self.version = NamedAPIResource(**version)


@dataclass
class PokemonHeldItem:
    item: NamedAPIResource["Item"]
    version_details: List["PokemonHeldItemVersion"]

    def __init__(self, item: Dict[str, Any], version_details: List[Dict[str, Any]]):
        self.item = NamedAPIResource(**item)
        self.version_details = [
            PokemonHeldItemVersion(**version) for version in version_details
        ]


@dataclass
class PokemonMoveVersion:
    level_learned_at: int
    version_group: NamedAPIResource["MoveLearnMethod"]
    move_learn_method: NamedAPIResource["MoveLearnMethod"]

    def __init__(
        self,
        level_learned_at: int,
        version_group: Dict[str, Any],
        move_learn_method: Dict[str, Any],
    ):
        self.level_learned_at = level_learned_at
        self.version_group = NamedAPIResource(**version_group)
        self.move_learn_method = NamedAPIResource(**move_learn_method)


@dataclass
class PokemonMove:
    move: NamedAPIResource["Move"]
    version_group_details: List[PokemonMoveVersion]

    def __init__(
        self, move: Dict[str, Any], version_group_details: List[Dict[str, Any]]
    ):
        self.move = NamedAPIResource(**move)
        self.version_group_details = [
            PokemonMoveVersion(**version) for version in version_group_details
        ]


@dataclass
class PokemonType:
    slot: int
    type: NamedAPIResource["Type"]

    def __init__(self, slot: int, type: Dict[str, Any]):
        self.slot = slot
        self.type = NamedAPIResource(**type)


@dataclass
class PokemonTypePast:
    generation: NamedAPIResource["Generation"]
    types: List[PokemonType]

    def __init__(self, generation: Dict[str, Any], types: List[Dict[str, Any]]):
        self.generation = NamedAPIResource(**generation)
        self.types = [PokemonType(**type) for type in types]


@dataclass
class PokemonSprites:
    back_default: str
    back_female: str
    back_shiny: str
    back_shiny_female: str
    front_default: str
    front_female: str
    front_shiny: str
    front_shiny_female: str

    def __init__(
        self,
        back_default: str,
        back_female: str,
        back_shiny: str,
        back_shiny_female: str,
        front_default: str,
        front_female: str,
        front_shiny: str,
        front_shiny_female: str,
        **kwargs,  # other and versions JSON data not handled yet
    ):
        self.back_default = back_default
        self.back_female = back_female
        self.back_shiny = back_shiny
        self.back_shiny_female = back_shiny_female
        self.front_default = front_default
        self.front_female = front_female
        self.front_shiny = front_shiny
        self.front_shiny_female = front_shiny_female


@dataclass
class PokemonStat:
    base_stat: int
    effort: int
    stat: NamedAPIResource["Stat"]

    def __init__(self, base_stat: int, effort: int, stat: Dict[str, Any]):
        self.base_stat = base_stat
        self.effort = effort
        self.stat = NamedAPIResource(**stat)


@dataclass
class Pokemon(CommonResource):
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[PokemonAbility]
    forms: List[NamedAPIResource["PokemonForm"]]
    game_indices: List[VersionGameIndex]
    held_items: List[PokemonHeldItem]
    location_area_encounters: str
    moves: List[PokemonMove]
    species: NamedAPIResource["PokemonSpecies"]
    sprites: PokemonSprites
    cries: PokemonCries
    stats: List[PokemonStat]
    types: List[PokemonType]
    past_types: List[PokemonTypePast]

    def __init__(
        self,
        id: int,
        name: str,
        base_experience: int,
        height: int,
        is_default: bool,
        order: int,
        weight: int,
        abilities: List[Dict[str, Any]],
        forms: List[Dict[str, Any]],
        game_indices: List[Dict[str, Any]],
        held_items: List[Dict[str, Any]],
        location_area_encounters: str,
        moves: List[Dict[str, Any]],
        species: Dict[str, Any],
        sprites: Dict[str, Any],
        cries: Dict[str, Any],
        stats: List[Dict[str, Any]],
        types: List[Dict[str, Any]],
        past_types: List[Dict[str, Any]],
        **kwargs,  # Capture additional keyword arguments
    ):
        super().__init__(id=id, name=name)
        self.base_experience = base_experience
        self.height = height
        self.is_default = is_default
        self.order = order
        self.weight = weight
        self.abilities = [PokemonAbility(**ability) for ability in abilities]
        self.forms = [NamedAPIResource(**form) for form in forms]
        self.game_indices = [VersionGameIndex(**index) for index in game_indices]
        self.held_items = [PokemonHeldItem(**item) for item in held_items]
        self.location_area_encounters = location_area_encounters
        self.moves = [PokemonMove(**move) for move in moves]
        self.species = NamedAPIResource(**species)
        self.sprites = PokemonSprites(**sprites)
        self.cries = PokemonCries(**cries)
        self.stats = [PokemonStat(**stat) for stat in stats]
        self.types = [PokemonType(**type) for type in types]
        self.past_types = [PokemonTypePast(**type_past) for type_past in past_types]

        # Handle unexpected keyword arguments
        # for key, value in kwargs.items():
        #     setattr(self, key, value)

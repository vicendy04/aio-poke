from dataclasses import dataclass
from typing import Any, Dict, List

from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    VersionGameIndex,
)


@dataclass
class PokemonAbility:
    is_hidden: bool
    slot: int
    ability: AdditionalResource

    def __init__(self, is_hidden: bool, slot: int, ability: Dict[str, Any]):
        self.is_hidden = is_hidden
        self.slot = slot
        self.ability = AdditionalResource(**ability)


@dataclass
class PokemonCries:
    latest: str
    legacy: str


@dataclass
class PokemonHeldItemVersion:
    rarity: int
    version: AdditionalResource

    def __init__(self, rarity: int, version: Dict[str, Any]):
        self.rarity = rarity
        self.version = AdditionalResource(**version)


@dataclass
class PokemonHeldItem:
    item: AdditionalResource
    version_details: List[PokemonHeldItemVersion]

    def __init__(self, item: Dict[str, Any], version_details: List[Dict[str, Any]]):
        self.item = AdditionalResource(**item)
        self.version_details = [
            PokemonHeldItemVersion(**version) for version in version_details
        ]


@dataclass
class PokemonMoveVersion:
    level_learned_at: int
    version_group: AdditionalResource
    move_learn_method: AdditionalResource

    def __init__(
        self,
        level_learned_at: int,
        version_group: Dict[str, Any],
        move_learn_method: Dict[str, Any],
    ):
        self.level_learned_at = level_learned_at
        self.version_group = AdditionalResource(**version_group)
        self.move_learn_method = AdditionalResource(**move_learn_method)


@dataclass
class PokemonMove:
    move: AdditionalResource
    version_group_details: List[PokemonMoveVersion]

    def __init__(
        self, move: Dict[str, Any], version_group_details: List[Dict[str, Any]]
    ):
        self.move = AdditionalResource(**move)
        self.version_group_details = [
            PokemonMoveVersion(**version) for version in version_group_details
        ]


@dataclass
class PokemonType:
    slot: int
    type: AdditionalResource

    def __init__(self, slot: int, type: Dict[str, Any]):
        self.slot = slot
        self.type = AdditionalResource(**type)


@dataclass
class PokemonTypePast:
    generation: AdditionalResource
    types: List[PokemonType]

    def __init__(self, generation: Dict[str, Any], types: List[Dict[str, Any]]):
        self.generation = AdditionalResource(**generation)
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
        **kwargs,  # other and versions JSON data not handle yet
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
    stat: AdditionalResource

    def __init__(self, base_stat: int, effort: int, stat: Dict[str, Any]):
        self.base_stat = base_stat
        self.effort = effort
        self.stat = AdditionalResource(**stat)


@dataclass
class Pokemon(CommonResource):
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[PokemonAbility]
    forms: List[AdditionalResource]
    game_indices: List[VersionGameIndex]
    held_items: List[PokemonHeldItem]
    location_area_encounters: str
    moves: List[PokemonMove]
    species: AdditionalResource
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
        self.forms = [AdditionalResource(**form) for form in forms]
        self.game_indices = [VersionGameIndex(**index) for index in game_indices]
        self.held_items = [PokemonHeldItem(**item) for item in held_items]
        self.location_area_encounters = location_area_encounters
        self.moves = [PokemonMove(**move) for move in moves]
        self.species = AdditionalResource(**species)
        self.sprites = PokemonSprites(**sprites)
        self.cries = PokemonCries(**cries)
        self.stats = [PokemonStat(**stat) for stat in stats]
        self.types = [PokemonType(**type) for type in types]
        self.past_types = [PokemonTypePast(**type_past) for type_past in past_types]

        # Handle unexpected keyword arguments
        # for key, value in kwargs.items():
        #     setattr(self, key, value)

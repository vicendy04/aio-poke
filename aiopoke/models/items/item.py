from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    APIResource,
    AdditionalResource,
    CommonResource,
    Description,
    Effect,
    GenerationGameIndex,
    MachineVersionDetail,
    Name,
    VerboseEffect,
    VersionGroupFlavorText,
)


@dataclass
class ItemFlingEffect(CommonResource):
    effect_entries: List[Effect]
    items: List[AdditionalResource]


@dataclass
class FlavorTextEntry:
    text: str
    version_group: ItemFlingEffect
    language: ItemFlingEffect


@dataclass
class GameIndex:
    game_index: int
    generation: ItemFlingEffect


@dataclass
class ItemHolderPokemonVersionDetail:
    rarity: int
    version: AdditionalResource


@dataclass
class ItemHolderPokemon:
    pokemon: AdditionalResource
    version_details: List[ItemHolderPokemonVersionDetail]


@dataclass
class ItemSprites:
    default: str


@dataclass
class ItemAttribute(CommonResource):
    descriptions: List[Description]
    items: List[AdditionalResource]
    names: List[Name]


@dataclass
class Item(CommonResource):
    cost: int
    fling_power: int
    fling_effect: AdditionalResource
    attributes: List[AdditionalResource]

    category: AdditionalResource
    effect_entries: List[VerboseEffect]
    flavor_text_entries: List[VersionGroupFlavorText]
    game_indices: List[GenerationGameIndex]
    names: List[Name]
    sprites: ItemSprites
    held_by_pokemon: List[ItemHolderPokemon]

    baby_trigger_for: APIResource

    machines: List[MachineVersionDetail]

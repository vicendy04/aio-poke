from dataclasses import dataclass
from typing import List

from aiopoke.models.games.version import Version
from aiopoke.models.items.item_attributes import ItemAttribute
from aiopoke.models.items.item_categories import ItemCategory
from aiopoke.models.items.item_fling_effects import ItemFlingEffect
from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.utility.common_model import (
    Resource,
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
    version: AdditionalResource[Version]


@dataclass
class ItemHolderPokemon:
    pokemon: AdditionalResource[Pokemon]
    version_details: List[ItemHolderPokemonVersionDetail]


@dataclass
class ItemSprites:
    default: str


@dataclass
class Item(CommonResource):
    cost: int
    fling_power: int
    fling_effect: AdditionalResource[ItemFlingEffect]
    attributes: List[AdditionalResource[ItemAttribute]]

    category: AdditionalResource[ItemCategory]
    effect_entries: List[VerboseEffect]
    flavor_text_entries: List[VersionGroupFlavorText]
    game_indices: List[GenerationGameIndex]
    names: List[Name]
    sprites: ItemSprites
    held_by_pokemon: List[ItemHolderPokemon]

    baby_trigger_for: Resource

    machines: List[MachineVersionDetail]

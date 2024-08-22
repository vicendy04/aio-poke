from dataclasses import dataclass
from typing import List

from aiopoke.models.evolution.evolution_chains import EvolutionChain
from aiopoke.models.games.version import Version
from aiopoke.models.items.item_attributes import ItemAttribute
from aiopoke.models.items.item_categories import ItemCategory
from aiopoke.models.items.item_fling_effects import ItemFlingEffect
from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.utility.common_model import (
    UnnamedAPIResource,
    NamedAPIResource,
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
    version: NamedAPIResource[Version]


@dataclass
class ItemHolderPokemon:
    pokemon: NamedAPIResource[Pokemon]
    version_details: List[ItemHolderPokemonVersionDetail]


@dataclass
class ItemSprites:
    default: str


@dataclass
class Item(CommonResource):
    cost: int
    fling_power: int
    fling_effect: NamedAPIResource[ItemFlingEffect]
    attributes: List[NamedAPIResource[ItemAttribute]]
    category: NamedAPIResource[ItemCategory]
    effect_entries: List[VerboseEffect]
    flavor_text_entries: List[VersionGroupFlavorText]
    game_indices: List[GenerationGameIndex]
    names: List[Name]
    sprites: ItemSprites
    held_by_pokemon: List[ItemHolderPokemon]
    baby_trigger_for: UnnamedAPIResource[EvolutionChain]
    machines: List[MachineVersionDetail]

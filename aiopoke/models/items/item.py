from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    GenerationGameIndex,
    MachineVersionDetail,
    Name,
    NamedAPIResource,
    UnnamedAPIResource,
    VerboseEffect,
    VersionGroupFlavorText,
)

if TYPE_CHECKING:
    from aiopoke.models.evolution.evolution_chains import EvolutionChain
    from aiopoke.models.games.version import Version
    from aiopoke.models.items.item_attributes import ItemAttribute
    from aiopoke.models.items.item_categories import ItemCategory
    from aiopoke.models.items.item_fling_effects import ItemFlingEffect
    from aiopoke.models.pokemon.pokemon import Pokemon


@dataclass
class GameIndex:
    game_index: int
    generation: "ItemFlingEffect"

    def __init__(
        self,
        *,
        game_index: int,
        generation: Dict[str, Any],
    ) -> None:
        self.game_index = game_index
        self.generation = ItemFlingEffect(**generation)


@dataclass
class ItemHolderPokemonVersionDetail:
    rarity: int
    version: NamedAPIResource["Version"]

    def __init__(
        self,
        *,
        rarity: int,
        version: Dict[str, Any],
    ) -> None:
        self.rarity = rarity
        self.version = NamedAPIResource(**version)


@dataclass
class ItemHolderPokemon:
    pokemon: NamedAPIResource["Pokemon"]
    version_details: List["ItemHolderPokemonVersionDetail"]

    def __init__(
        self,
        *,
        pokemon: Dict[str, Any],
        version_details: List[Dict[str, Any]],
    ) -> None:
        self.pokemon = NamedAPIResource(**pokemon)
        self.version_details = (
            [ItemHolderPokemonVersionDetail(**detail) for detail in version_details]
            if version_details
            else []
        )


@dataclass
class ItemSprites:
    default: str


@dataclass
class Item(CommonResource):
    cost: int
    fling_power: int
    fling_effect: NamedAPIResource["ItemFlingEffect"]
    attributes: List["NamedAPIResource[ItemAttribute]"]
    category: NamedAPIResource["ItemCategory"]
    effect_entries: List["VerboseEffect"]
    flavor_text_entries: List["VersionGroupFlavorText"]
    game_indices: List["GenerationGameIndex"]
    names: List["Name"]
    sprites: ItemSprites
    held_by_pokemon: List["ItemHolderPokemon"]
    baby_trigger_for: UnnamedAPIResource["EvolutionChain"]
    machines: List["MachineVersionDetail"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        cost: int,
        fling_power: int,
        fling_effect: Dict[str, Any],
        attributes: List[Dict[str, Any]],
        category: Dict[str, Any],
        effect_entries: List[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
        game_indices: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
        sprites: Dict[str, Any],
        held_by_pokemon: List[Dict[str, Any]],
        baby_trigger_for: Dict[str, Any],
        machines: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.cost = cost
        self.fling_power = fling_power
        self.fling_effect = NamedAPIResource(**fling_effect)
        self.attributes = (
            [NamedAPIResource(**attribute) for attribute in attributes]
            if attributes
            else []
        )
        self.category = NamedAPIResource(**category)
        self.effect_entries = (
            [VerboseEffect(**entry) for entry in effect_entries]
            if effect_entries
            else []
        )
        self.flavor_text_entries = (
            [VersionGroupFlavorText(**entry) for entry in flavor_text_entries]
            if flavor_text_entries
            else []
        )
        self.game_indices = (
            [GenerationGameIndex(**index) for index in game_indices]
            if game_indices
            else []
        )
        self.names = [Name(**name) for name in names] if names else []
        self.sprites = ItemSprites(**sprites)
        self.held_by_pokemon = (
            [ItemHolderPokemon(**pokemon) for pokemon in held_by_pokemon]
            if held_by_pokemon
            else []
        )
        self.baby_trigger_for = UnnamedAPIResource(**baby_trigger_for)
        self.machines = (
            [MachineVersionDetail(**machine) for machine in machines]
            if machines
            else []
        )

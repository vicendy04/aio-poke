from dataclasses import dataclass
from typing import List

from aiopoke.models.evolution.evolution_chains import EvolutionChain
from aiopoke.models.games.generations import Generation
from aiopoke.models.games.pokedexs import Pokedex
from aiopoke.models.locations.pal_park_areas import PalParkArea
from aiopoke.models.pokemon.egg_groups import EggGroup
from aiopoke.models.pokemon.growth_rates import GrowthRate
from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.pokemon.pokemon_colors import PokemonColor
from aiopoke.models.pokemon.pokemon_habitats import PokemonHabitat
from aiopoke.models.pokemon.pokemon_shapes import PokemonShape
from aiopoke.models.utility.common_model import (
    Resource,
    AdditionalResource,
    CommonResource,
    Description,
    FlavorText,
    Name,
)
from aiopoke.models.utility.languages import Language


@dataclass
class Genus:
    genus: str
    language: AdditionalResource[Language]


@dataclass
class PokemonSpeciesDexEntry:
    entry_number: int
    pokedex: AdditionalResource[Pokedex]


@dataclass
class PokemonSpeciesVariety:
    is_default: bool
    pokemon: AdditionalResource[Pokemon]


@dataclass
class PalParkEncounterArea:
    base_score: int
    rate: int
    area: AdditionalResource[PalParkArea]


@dataclass
class PokemonSpecies(CommonResource):
    order: int
    gender_rate: int
    capture_rate: int
    base_happiness: int
    is_baby: bool
    is_legendary: bool
    is_mythical: bool
    hatch_counter: int
    has_gender_differences: bool
    forms_switchable: bool
    growth_rate: AdditionalResource[GrowthRate]
    pokedex_numbers: List[PokemonSpeciesDexEntry]
    egg_groups: List[AdditionalResource[EggGroup]]
    color: AdditionalResource[PokemonColor]
    shape: AdditionalResource[PokemonShape]
    evolves_from_species: AdditionalResource["PokemonSpecies"]

    # here
    evolution_chain: Resource

    habitat: AdditionalResource[PokemonHabitat]
    generation: AdditionalResource[Generation]
    names: List[Name]
    flavor_text_entries: List[FlavorText]
    form_descriptions: List[Description]
    genera: List[Genus]
    varieties: List[PokemonSpeciesVariety]
    pal_park_encounters: List["PalParkEncounterArea"]

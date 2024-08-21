from dataclasses import dataclass
from typing import List

from aiopoke.models.evolution.evolution_chains import EvolutionChain
from aiopoke.models.utility.common_models import (
    APIResource,
    AdditionalResource,
    CommonResource,
    Description,
    FlavorText,
    Name,
)


@dataclass
class Genus:
    genus: str
    language: AdditionalResource


@dataclass
class PokemonSpeciesDexEntry:
    entry_number: int
    pokedex: AdditionalResource


@dataclass
class PokemonSpeciesVariety:
    is_default: bool
    pokemon: AdditionalResource


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
    growth_rate: AdditionalResource
    pokedex_numbers: List[PokemonSpeciesDexEntry]
    egg_groups: List[AdditionalResource]
    color: AdditionalResource
    shape: AdditionalResource
    evolves_from_species: AdditionalResource
    evolution_chain: APIResource
    habitat: AdditionalResource
    generation: AdditionalResource
    names: List[Name]
    flavor_text_entries: List[FlavorText]
    form_descriptions: List[Description]
    genera: List[Genus]
    varieties: List[PokemonSpeciesVariety]

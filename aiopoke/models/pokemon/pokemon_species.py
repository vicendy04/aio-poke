from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
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
    CommonResource,
    Description,
    FlavorText,
    Name,
    NamedAPIResource,
    UnnamedAPIResource,
)
from aiopoke.models.utility.languages import Language


@dataclass
class Genus:
    genus: str
    language: NamedAPIResource["Language"]

    def __init__(
        self,
        *,
        genus: str,
        language: Dict[str, Any],
    ) -> None:
        self.genus = genus
        self.language = NamedAPIResource(**language)


@dataclass
class PokemonSpeciesDexEntry:
    entry_number: int
    pokedex: NamedAPIResource["Pokedex"]

    def __init__(
        self,
        *,
        entry_number: int,
        pokedex: Dict[str, Any],
    ) -> None:
        self.entry_number = entry_number
        self.pokedex = NamedAPIResource(**pokedex)


@dataclass
class PokemonSpeciesVariety:
    is_default: bool
    pokemon: NamedAPIResource["Pokemon"]

    def __init__(
        self,
        *,
        is_default: bool,
        pokemon: Dict[str, Any],
    ) -> None:
        self.is_default = is_default
        self.pokemon = NamedAPIResource(**pokemon)


@dataclass
class PalParkEncounterArea:
    base_score: int
    rate: int
    area: NamedAPIResource["PalParkArea"]

    def __init__(
        self,
        *,
        base_score: int,
        rate: int,
        area: Dict[str, Any],
    ) -> None:
        self.base_score = base_score
        self.rate = rate
        self.area = NamedAPIResource(**area)


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
    growth_rate: NamedAPIResource[GrowthRate]
    pokedex_numbers: List[PokemonSpeciesDexEntry]
    egg_groups: List[NamedAPIResource[EggGroup]]
    color: NamedAPIResource[PokemonColor]
    shape: NamedAPIResource[PokemonShape]
    evolves_from_species: NamedAPIResource["PokemonSpecies"]
    evolution_chain: UnnamedAPIResource[EvolutionChain]
    habitat: NamedAPIResource[PokemonHabitat]
    generation: NamedAPIResource[Generation]
    names: List[Name]
    flavor_text_entries: List[FlavorText]
    form_descriptions: List[Description]
    genera: List[Genus]
    varieties: List[PokemonSpeciesVariety]
    pal_park_encounters: List["PalParkEncounterArea"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        order: int,
        gender_rate: int,
        capture_rate: int,
        base_happiness: int,
        is_baby: bool,
        is_legendary: bool,
        is_mythical: bool,
        hatch_counter: int,
        has_gender_differences: bool,
        forms_switchable: bool,
        growth_rate: Dict[str, Any],
        pokedex_numbers: List[Dict[str, Any]],
        egg_groups: List[Dict[str, Any]],
        color: Dict[str, Any],
        shape: Dict[str, Any],
        evolves_from_species: Dict[str, Any],
        evolution_chain: Dict[str, Any],
        habitat: Dict[str, Any],
        generation: Dict[str, Any],
        names: List[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
        form_descriptions: List[Dict[str, Any]],
        genera: List[Dict[str, Any]],
        varieties: List[Dict[str, Any]],
        pal_park_encounters: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.order = order
        self.gender_rate = gender_rate
        self.capture_rate = capture_rate
        self.base_happiness = base_happiness
        self.is_baby = is_baby
        self.is_legendary = is_legendary
        self.is_mythical = is_mythical
        self.hatch_counter = hatch_counter
        self.has_gender_differences = has_gender_differences
        self.forms_switchable = forms_switchable
        self.growth_rate = NamedAPIResource(**growth_rate)
        self.pokedex_numbers = (
            [PokemonSpeciesDexEntry(**entry) for entry in pokedex_numbers]
            if pokedex_numbers
            else []
        )
        self.egg_groups = (
            [NamedAPIResource(**egg_group) for egg_group in egg_groups]
            if egg_groups
            else []
        )
        self.color = NamedAPIResource(**color)
        self.shape = NamedAPIResource(**shape)
        self.evolves_from_species = NamedAPIResource(**evolves_from_species)
        self.evolution_chain = UnnamedAPIResource(**evolution_chain)
        self.habitat = NamedAPIResource(**habitat)
        self.generation = NamedAPIResource(**generation)
        self.names = [Name(**name) for name in names] if names else []
        self.flavor_text_entries = (
            [FlavorText(**text) for text in flavor_text_entries]
            if flavor_text_entries
            else []
        )
        self.form_descriptions = (
            [Description(**description) for description in form_descriptions]
            if form_descriptions
            else []
        )
        self.genera = [Genus(**genus) for genus in genera] if genera else []
        self.varieties = (
            [PokemonSpeciesVariety(**variety) for variety in varieties]
            if varieties
            else []
        )
        self.pal_park_encounters = (
            [PalParkEncounterArea(**encounter) for encounter in pal_park_encounters]
            if pal_park_encounters
            else []
        )

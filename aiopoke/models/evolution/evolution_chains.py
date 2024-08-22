from dataclasses import dataclass
from typing import List, Optional

from aiopoke.models.utility.common_model import NamedAPIResource


@dataclass
class EvolutionDetail:
    gender: Optional[int]
    held_item: Optional[NamedAPIResource]
    item: Optional[NamedAPIResource]
    known_move: Optional[NamedAPIResource]
    known_move_type: Optional[NamedAPIResource]
    location: Optional[NamedAPIResource]
    min_affection: Optional[int]
    min_beauty: Optional[int]
    min_happiness: Optional[int]
    min_level: int
    needs_overworld_rain: Optional[bool]
    party_species: Optional[NamedAPIResource]
    party_type: Optional[NamedAPIResource]
    relative_physical_stats: Optional[int]
    time_of_day: str
    trade_species: Optional[NamedAPIResource]
    trigger: NamedAPIResource
    turn_upside_down: bool


@dataclass
class ChainLink:
    is_baby: bool
    species: NamedAPIResource
    evolution_details: List[EvolutionDetail]
    evolves_to: List["ChainLink"]


@dataclass
class EvolutionChain:
    id: int
    baby_trigger_item: NamedAPIResource
    chain: "ChainLink"

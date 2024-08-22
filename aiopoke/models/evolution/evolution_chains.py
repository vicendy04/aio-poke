from dataclasses import dataclass
from typing import List, Optional

from aiopoke.models.utility.common_model import AdditionalResource


@dataclass
class EvolutionDetail:
    gender: Optional[int]
    held_item: Optional[AdditionalResource]
    item: Optional[AdditionalResource]
    known_move: Optional[AdditionalResource]
    known_move_type: Optional[AdditionalResource]
    location: Optional[AdditionalResource]
    min_affection: Optional[int]
    min_beauty: Optional[int]
    min_happiness: Optional[int]
    min_level: int
    needs_overworld_rain: Optional[bool]
    party_species: Optional[AdditionalResource]
    party_type: Optional[AdditionalResource]
    relative_physical_stats: Optional[int]
    time_of_day: str
    trade_species: Optional[AdditionalResource]
    trigger: AdditionalResource
    turn_upside_down: bool


@dataclass
class ChainLink:
    is_baby: bool
    species: AdditionalResource
    evolution_details: List[EvolutionDetail]
    evolves_to: List["ChainLink"]


@dataclass
class EvolutionChain:
    id: int
    baby_trigger_item: AdditionalResource
    chain: "ChainLink"

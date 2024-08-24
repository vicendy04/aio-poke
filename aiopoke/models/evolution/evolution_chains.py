from dataclasses import dataclass
from typing import Any, Dict, List, Optional

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

    def __init__(
        self,
        *,
        gender: Optional[int] = None,
        held_item: Optional[Dict[str, Any]] = None,
        item: Optional[Dict[str, Any]] = None,
        known_move: Optional[Dict[str, Any]] = None,
        known_move_type: Optional[Dict[str, Any]] = None,
        location: Optional[Dict[str, Any]] = None,
        min_affection: Optional[int] = None,
        min_beauty: Optional[int] = None,
        min_happiness: Optional[int] = None,
        min_level: int,
        needs_overworld_rain: Optional[bool] = None,
        party_species: Optional[Dict[str, Any]] = None,
        party_type: Optional[Dict[str, Any]] = None,
        relative_physical_stats: Optional[int] = None,
        time_of_day: str,
        trade_species: Optional[Dict[str, Any]] = None,
        trigger: Dict[str, Any],
        turn_upside_down: bool,
    ) -> None:
        self.gender = gender
        self.held_item = NamedAPIResource(**held_item) if held_item else None
        self.item = NamedAPIResource(**item) if item else None
        self.known_move = NamedAPIResource(**known_move) if known_move else None
        self.known_move_type = (
            NamedAPIResource(**known_move_type) if known_move_type else None
        )
        self.location = NamedAPIResource(**location) if location else None
        self.min_affection = min_affection
        self.min_beauty = min_beauty
        self.min_happiness = min_happiness
        self.min_level = min_level
        self.needs_overworld_rain = needs_overworld_rain
        self.party_species = (
            NamedAPIResource(**party_species) if party_species else None
        )
        self.party_type = NamedAPIResource(**party_type) if party_type else None
        self.relative_physical_stats = relative_physical_stats
        self.time_of_day = time_of_day
        self.trade_species = (
            NamedAPIResource(**trade_species) if trade_species else None
        )
        self.trigger = NamedAPIResource(**trigger)
        self.turn_upside_down = turn_upside_down


@dataclass
class ChainLink:
    is_baby: bool
    species: NamedAPIResource
    evolution_details: List[EvolutionDetail]
    evolves_to: List["ChainLink"]

    def __init__(
        self,
        *,
        is_baby: bool,
        species: Dict[str, Any],
        evolution_details: List[Dict[str, Any]],
        evolves_to: List[Dict[str, Any]],
    ) -> None:
        self.is_baby = is_baby
        self.species = NamedAPIResource(**species)
        self.evolution_details = (
            [EvolutionDetail(**detail) for detail in evolution_details]
            if evolution_details
            else []
        )
        self.evolves_to = [ChainLink(**e) for e in evolves_to] if evolves_to else []


@dataclass
class EvolutionChain:
    id: int
    baby_trigger_item: NamedAPIResource
    chain: "ChainLink"

    def __init__(
        self,
        *,
        id: int,
        baby_trigger_item: Dict[str, Any],
        chain: Dict[str, Any],
    ) -> None:
        self.id = id
        self.baby_trigger_item = NamedAPIResource(**baby_trigger_item)
        self.chain = ChainLink(**chain)

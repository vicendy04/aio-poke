from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.utility.common_model import Effect, FlavorText


@dataclass
class ContestEffect:
    id: int
    appeal: int
    jam: int
    effect_entries: List["Effect"]
    flavor_text_entries: List["FlavorText"]

    def __init__(
        self,
        *,
        id: int,
        appeal: int,
        jam: int,
        effect_entries: List[Dict[str, Any]],
        flavor_text_entries: List[Dict[str, Any]],
    ) -> None:
        self.id = id
        self.appeal = appeal
        self.jam = jam
        self.effect_entries = (
            [Effect(**entry) for entry in effect_entries] if effect_entries else []
        )
        self.flavor_text_entries = (
            [FlavorText(**entry) for entry in flavor_text_entries]
            if flavor_text_entries
            else []
        )

from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import FlavorText, NamedAPIResource

if TYPE_CHECKING:
    from aiopoke.models.moves.moves import Move


class SuperContestEffect:
    id: int
    appeal: int
    flavor_text_entries: List["FlavorText"]
    moves: List["NamedAPIResource[Move]"]

    def __init__(
        self,
        *,
        id: int,
        appeal: int,
        flavor_text_entries: List[Dict[str, Any]],
        moves: List[Dict[str, Any]],
    ) -> None:
        self.id = id
        self.appeal = appeal
        self.flavor_text_entries = (
            [FlavorText(**entry) for entry in flavor_text_entries]
            if flavor_text_entries
            else []
        )
        self.moves = [NamedAPIResource(**move) for move in moves] if moves else []

from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import FlavorText, NamedAPIResource

if TYPE_CHECKING:
    from aiopoke.models.moves.moves import Move


class SuperContestEffect:
    id: int
    appeal: int
    flavor_text_entries: List["FlavorText"]
    moves: List["NamedAPIResource[Move]"]

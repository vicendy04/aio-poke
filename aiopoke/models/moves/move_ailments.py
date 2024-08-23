from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.moves.moves import Move
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


class MoveAilment(CommonResource):
    moves: List["NamedAPIResource[Move]"]
    names: List["Name"]

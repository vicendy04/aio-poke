from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.moves.moves import Move
from aiopoke.models.utility.common_model import (
    CommonResource,
    Description,
    NamedAPIResource,
)


class MoveCategory(CommonResource):
    descriptions: List["Description"]
    moves: List["NamedAPIResource[Move]"]

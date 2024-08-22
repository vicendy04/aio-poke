from typing import List
from aiopoke.models.moves.moves import Move
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Name,
)


class MoveAilment(CommonResource):
    moves: List[NamedAPIResource[Move]]
    names: List[Name]

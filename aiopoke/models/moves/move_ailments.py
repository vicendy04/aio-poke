from typing import List
from aiopoke.models.moves.moves import Move
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Name,
)


class MoveAilment(CommonResource):
    moves: List[AdditionalResource[Move]]
    names: List[Name]

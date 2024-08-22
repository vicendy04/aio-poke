from typing import List
from aiopoke.models.moves.moves import Move
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Description,
)


class MoveCategory(CommonResource):
    descriptions: List[Description]
    moves: List[AdditionalResource[Move]]

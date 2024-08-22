from dataclasses import dataclass
from typing import List

from aiopoke.models.moves.moves import Move
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Description,
    Name,
)


@dataclass
class MoveDamageClass(CommonResource):
    descriptions: List[Description]
    moves: List[AdditionalResource[Move]]
    names: List[Name]

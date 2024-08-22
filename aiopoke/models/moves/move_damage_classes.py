from dataclasses import dataclass
from typing import List

from aiopoke.models.moves.moves import Move
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Description,
    Name,
)


@dataclass
class MoveDamageClass(CommonResource):
    descriptions: List[Description]
    moves: List[NamedAPIResource[Move]]
    names: List[Name]

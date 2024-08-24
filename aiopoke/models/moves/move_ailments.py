from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        moves: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.moves = [NamedAPIResource(**move) for move in moves] if moves else []
        self.names = [Name(**name) for name in names] if names else []

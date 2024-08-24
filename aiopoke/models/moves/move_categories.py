from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        descriptions: List[Dict[str, Any]],
        moves: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.descriptions = (
            [Description(**description) for description in descriptions]
            if descriptions
            else []
        )
        self.moves = [NamedAPIResource(**move) for move in moves] if moves else []

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict

if TYPE_CHECKING:
    from aiopoke.models.games.version_groups import VersionGroup
    from aiopoke.models.items.item import Item
    from aiopoke.models.moves.moves import Move

from aiopoke.models.utility.common_model import NamedAPIResource


@dataclass
class Machine:
    id: int
    item: NamedAPIResource["Item"]
    move: NamedAPIResource["Move"]
    version_group: NamedAPIResource["VersionGroup"]

    def __init__(
        self,
        *,
        id: int,
        item: Dict[str, Any],
        move: Dict[str, Any],
        version_group: Dict[str, Any],
    ) -> None:
        self.id = id
        self.item = NamedAPIResource(**item)
        self.move = NamedAPIResource(**move)
        self.version_group = NamedAPIResource(**version_group)

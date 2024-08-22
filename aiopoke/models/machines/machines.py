from dataclasses import dataclass

from aiopoke.models.games.version_groups import VersionGroup
from aiopoke.models.items.item import Item
from aiopoke.models.moves.moves import Move
from aiopoke.models.utility.common_model import NamedAPIResource


@dataclass
class Machine:
    id: int
    item: NamedAPIResource[Item]
    move: NamedAPIResource[Move]
    version_group: NamedAPIResource[VersionGroup]

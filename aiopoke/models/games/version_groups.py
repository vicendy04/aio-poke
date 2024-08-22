from dataclasses import dataclass
from typing import List, TYPE_CHECKING

from aiopoke.models.games.version import Version
from aiopoke.models.locations.regions import Region
from aiopoke.models.moves.move_learn_methods import MoveLearnMethod
from aiopoke.models.utility.common_model import AdditionalResource, CommonResource

if TYPE_CHECKING:
    from aiopoke.models.games.generations import Generation
    from aiopoke.models.games.pokedexs import Pokedex


@dataclass
class VersionGroup(CommonResource):
    order: int
    generation: "AdditionalResource['Generation']"
    move_learn_methods: List[AdditionalResource[MoveLearnMethod]]
    pokedexes: List[AdditionalResource[Pokedex]]
    regions: List[AdditionalResource[Region]]
    versions: AdditionalResource[Version]

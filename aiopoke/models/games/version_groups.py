from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import CommonResource, NamedAPIResource

if TYPE_CHECKING:
    from aiopoke.models.games.generations import Generation
    from aiopoke.models.games.pokedexs import Pokedex
    from aiopoke.models.games.version import Version
    from aiopoke.models.locations.regions import Region
    from aiopoke.models.moves.move_learn_methods import MoveLearnMethod


@dataclass
class VersionGroup(CommonResource):
    order: int
    generation: NamedAPIResource["Generation"]
    move_learn_methods: List["NamedAPIResource[MoveLearnMethod]"]
    pokedexes: List["NamedAPIResource[Pokedex]"]
    regions: List["NamedAPIResource[Region]"]
    versions: NamedAPIResource["Version"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        order: int,
        generation: Dict[str, Any],
        move_learn_methods: List[Dict[str, Any]],
        pokedexes: List[Dict[str, Any]],
        regions: List[Dict[str, Any]],
        versions: Dict[str, Any],
    ) -> None:
        super().__init__(id=id, name=name)
        self.order = order
        self.generation = NamedAPIResource(**generation)
        self.move_learn_methods = (
            [NamedAPIResource(**method) for method in move_learn_methods]
            if move_learn_methods
            else []
        )
        self.pokedexes = (
            [NamedAPIResource(**pokedex) for pokedex in pokedexes] if pokedexes else []
        )
        self.regions = (
            [NamedAPIResource(**region) for region in regions] if regions else []
        )
        self.versions = NamedAPIResource(**versions)

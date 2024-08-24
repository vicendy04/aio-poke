from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.natures import Nature
from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)


@dataclass
class NaturePokeathlonStatAffect:
    max_change: int
    nature: NamedAPIResource["Nature"]

    def __init__(
        self,
        *,
        max_change: int,
        nature: Dict[str, Any],
    ) -> None:
        self.max_change = max_change
        self.nature = NamedAPIResource(**nature)


@dataclass
class NaturePokeathlonStatAffectSets:
    increase: List["NaturePokeathlonStatAffect"]
    decrease: List["NaturePokeathlonStatAffect"]

    def __init__(
        self,
        *,
        increase: List[Dict[str, Any]],
        decrease: List[Dict[str, Any]],
    ) -> None:
        self.increase = (
            [NaturePokeathlonStatAffect(**affect) for affect in increase]
            if increase
            else []
        )
        self.decrease = (
            [NaturePokeathlonStatAffect(**affect) for affect in decrease]
            if decrease
            else []
        )


@dataclass
class PokeathlonStat(CommonResource):
    affecting_natures: NaturePokeathlonStatAffectSets
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        affecting_natures: Dict[str, Any],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.affecting_natures = NaturePokeathlonStatAffectSets(**affecting_natures)
        self.names = [Name(**name) for name in names] if names else []

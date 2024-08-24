from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.encounters.encounter_conditions import EncounterCondition


@dataclass
class EncounterConditionValue(CommonResource):
    condition: NamedAPIResource["EncounterCondition"]
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        condition: Dict[str, Any],
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.condition = NamedAPIResource(**condition)
        self.names = [Name(**name) for name in names] if names else []

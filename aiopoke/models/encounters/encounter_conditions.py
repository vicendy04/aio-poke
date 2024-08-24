from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import Name, NamedAPIResource

if TYPE_CHECKING:
    from aiopoke.models.encounters.encounter_condition_values import (
        EncounterConditionValue,
    )


@dataclass
class EncounterCondition:
    values: List["NamedAPIResource[EncounterConditionValue]"]
    names: List["Name"]

    def __init__(
        self,
        *,
        values: List[Dict[str, Any]],
        names: List[Dict[str, Any]],
    ) -> None:
        self.values = [NamedAPIResource(**value) for value in values] if values else []
        self.names = [Name(**name) for name in names] if names else []

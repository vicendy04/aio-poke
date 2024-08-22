from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import AdditionalResource, Name

if TYPE_CHECKING:
    from aiopoke.models.encounters.encounter_condition_values import (
        EncounterConditionValue,
    )


@dataclass
class EncounterCondition:
    values: List[AdditionalResource["EncounterConditionValue"]]
    names: List["Name"]

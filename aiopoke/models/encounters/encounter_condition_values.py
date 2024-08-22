from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Name,
)

if TYPE_CHECKING:
    from aiopoke.models.encounters.encounter_conditions import EncounterCondition


@dataclass
class EncounterConditionValue(CommonResource):
    condition: AdditionalResource["EncounterCondition"]
    names: List["Name"]

from dataclasses import dataclass
from typing import TYPE_CHECKING, List

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

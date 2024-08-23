from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import Name, NamedAPIResource

if TYPE_CHECKING:
    from aiopoke.models.encounters.encounter_condition_values import (
        EncounterConditionValue,
    )


@dataclass
class EncounterCondition:
    values: List["NamedAPIResource[EncounterConditionValue]"]
    names: List["Name"]

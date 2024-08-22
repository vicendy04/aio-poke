from dataclasses import dataclass
from typing import List
from aiopoke.models.utility.common_model import CommonResource, Name


@dataclass
class EncounterMethod(CommonResource):
    order: int
    names: List["Name"]

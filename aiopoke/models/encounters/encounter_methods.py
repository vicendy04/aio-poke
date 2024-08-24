from dataclasses import dataclass
from typing import Any, Dict, List

from aiopoke.models.utility.common_model import CommonResource, Name


@dataclass
class EncounterMethod(CommonResource):
    order: int
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        order: int,
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.order = order
        self.names = [Name(**name) for name in names] if names else []

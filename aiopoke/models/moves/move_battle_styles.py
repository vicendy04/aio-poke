from dataclasses import dataclass
from typing import Any, Dict, List

from aiopoke.models.utility.common_model import CommonResource, Name


@dataclass
class MoveBatteStyle(CommonResource):
    names: List["Name"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        names: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.names = [Name(**name) for name in names] if names else []

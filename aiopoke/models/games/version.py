from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.games.version_groups import VersionGroup


@dataclass
class Version(CommonResource):
    names: List["Name"]
    version_group: NamedAPIResource["VersionGroup"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        names: List[Dict[str, Any]],
        version_group: Dict[str, Any],
    ) -> None:
        super().__init__(id=id, name=name)
        self.names = [Name(**name) for name in names] if names else []
        self.version_group = NamedAPIResource(**version_group)

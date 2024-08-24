from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.games.version_groups import VersionGroup
from aiopoke.models.utility.common_model import (
    CommonResource,
    Description,
    Name,
    NamedAPIResource,
)


@dataclass
class MoveLearnMethod(CommonResource):
    names: List["Name"]
    descriptions: List["Description"]
    version_groups: List["NamedAPIResource[VersionGroup]"]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        names: List[Dict[str, Any]],
        descriptions: List[Dict[str, Any]],
        version_groups: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.names = [Name(**name) for name in names] if names else []
        self.descriptions = (
            [Description(**description) for description in descriptions]
            if descriptions
            else []
        )
        self.version_groups = (
            [NamedAPIResource(**version_group) for version_group in version_groups]
            if version_groups
            else []
        )

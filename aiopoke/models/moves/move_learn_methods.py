from dataclasses import dataclass
from typing import TYPE_CHECKING, List

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

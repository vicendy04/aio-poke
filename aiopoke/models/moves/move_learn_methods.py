from dataclasses import dataclass
from typing import List

from aiopoke.models.games.version_groups import VersionGroup
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    Description,
    Name,
)


@dataclass
class MoveLearnMethod(CommonResource):
    names: List[Name]
    descriptions: List[Description]
    version_groups: List[NamedAPIResource[VersionGroup]]

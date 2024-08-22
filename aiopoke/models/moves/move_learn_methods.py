from dataclasses import dataclass
from typing import List

from aiopoke.models.games.version_groups import VersionGroup
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    Description,
    Name,
)


@dataclass
class MoveLearnMethod(CommonResource):
    names: List[Name]
    descriptions: List[Description]
    version_groups: List[AdditionalResource[VersionGroup]]

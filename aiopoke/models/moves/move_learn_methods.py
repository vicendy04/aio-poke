from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Description,
    Name,
)


@dataclass
class MoveLearnMethod(CommonResource):
    names: List[Name]
    descriptions: List[Description]
    version_groups: AdditionalResource

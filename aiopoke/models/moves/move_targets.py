from typing import List
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Description,
    Name,
)


class MoveTarget(CommonResource):
    descriptions: List["Description"]
    moves: List[AdditionalResource]
    names: List["Name"]

from typing import List
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


class MoveAilment(CommonResource):
    moves: List[AdditionalResource]
    names: List[Name]

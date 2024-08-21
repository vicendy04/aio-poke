from typing import List
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Description,
)


class MoveCategory(CommonResource):
    descriptions: List[Description]
    moves: List[AdditionalResource]

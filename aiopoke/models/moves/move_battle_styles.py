from typing import List
from aiopoke.models.utility.common_models import CommonResource, Name


class MoveBatteStyle(CommonResource):
    names: List[Name]

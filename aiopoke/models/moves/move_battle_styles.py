from typing import List
from aiopoke.models.utility.common_model import CommonResource, Name


class MoveBatteStyle(CommonResource):
    names: List[Name]

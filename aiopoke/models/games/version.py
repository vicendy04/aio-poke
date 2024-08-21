from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class Version(CommonResource):
    names: List[Name]
    version_group: AdditionalResource

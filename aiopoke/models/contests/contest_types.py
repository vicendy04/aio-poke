from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import AdditionalResource, CommonResource


@dataclass
class ContestName:
    name: str
    color: str
    language: AdditionalResource


@dataclass
class ContestType(CommonResource):
    berry_flavor: AdditionalResource
    names: List[ContestName]

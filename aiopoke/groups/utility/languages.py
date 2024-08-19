from dataclasses import dataclass
from typing import List

from aiopoke.groups.utility.common_models import Name, IdentifiedResource


@dataclass
class Language(IdentifiedResource):
    official: bool
    iso639: str
    iso3166: str
    names: List[Name]

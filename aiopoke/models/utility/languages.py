from dataclasses import dataclass
from typing import Any, Dict, List

from aiopoke.models.utility.common_model import CommonResource, Name


@dataclass
class Language(CommonResource):
    official: bool
    iso3166: str
    iso639: str
    names: List["Name"]

    def __init__(
        self,
        id: int,
        name: str,
        official: bool,
        iso3166: str,
        iso639: str,
        names: List[Dict[str, Any]],
    ):
        super().__init__(id=id, name=name)
        self.official = official
        self.iso3166 = iso3166
        self.iso639 = iso639
        self.names = [Name(**name) for name in names]

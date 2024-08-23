from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.games.version_groups import VersionGroup


@dataclass
class Version(CommonResource):
    names: List["Name"]
    version_group: NamedAPIResource["VersionGroup"]

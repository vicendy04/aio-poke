from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    Name,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.berries.berries import Berry


@dataclass
class BerryFirmness(CommonResource):
    berries: List["NamedAPIResource[Berry]"]
    names: List["Name"]

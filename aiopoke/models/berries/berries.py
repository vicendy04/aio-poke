from dataclasses import dataclass
from typing import List

from aiopoke.models.berries.berry_flavors import BerryFlavor
from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    Name,
)


@dataclass
class BerryFirmness(CommonResource):
    berries: AdditionalResource
    names: List[Name]


@dataclass
class BerryFlavorMap:
    potency: int
    flavor: AdditionalResource


@dataclass
class Berry(CommonResource):
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int

    firmness: AdditionalResource
    flavors: List[BerryFlavorMap]

    item: AdditionalResource
    natural_gift_type: AdditionalResource

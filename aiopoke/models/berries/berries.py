from dataclasses import dataclass
from typing import List

from aiopoke.models.berries.berry_firmnesses import BerryFirmness
from aiopoke.models.berries.berry_flavors import BerryFlavor
from aiopoke.models.items.item import Item
from aiopoke.models.pokemon.types import Type
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
)


@dataclass
class BerryFlavorMap:
    potency: int
    flavor: AdditionalResource[BerryFlavor]


@dataclass
class Berry(CommonResource):
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: AdditionalResource[BerryFirmness]
    flavors: List[BerryFlavorMap]
    item: AdditionalResource[Item]
    natural_gift_type: AdditionalResource[Type]

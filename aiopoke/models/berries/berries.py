from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from aiopoke.models.utility.common_model import (
    CommonResource,
    NamedAPIResource,
)

if TYPE_CHECKING:
    from aiopoke.models.berries.berry_firmnesses import BerryFirmness
    from aiopoke.models.berries.berry_flavors import BerryFlavor
    from aiopoke.models.items.item import Item
    from aiopoke.models.pokemon.types import Type


@dataclass
class BerryFlavorMap:
    potency: int
    flavor: NamedAPIResource["BerryFlavor"]


@dataclass
class Berry(CommonResource):
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: NamedAPIResource["BerryFirmness"]
    flavors: List["BerryFlavorMap"]
    item: NamedAPIResource["Item"]
    natural_gift_type: NamedAPIResource["Type"]

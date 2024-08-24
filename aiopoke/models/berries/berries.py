from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

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

    def __init__(self, potency: int, flavor: Dict[str, Any]) -> None:
        self.potency = potency
        self.flavor = NamedAPIResource(**flavor)


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

    def __init__(
        self,
        *,
        id: int,
        name: str,
        growth_time: int,
        max_harvest: int,
        natural_gift_power: int,
        size: int,
        smoothness: int,
        soil_dryness: int,
        firmness: Dict[str, Any],
        flavors: List[Dict[str, Any]],
        item: Dict[str, Any],
        natural_gift_type: Dict[str, Any],
    ) -> None:
        super().__init__(id=id, name=name)
        self.growth_time = growth_time
        self.max_harvest = max_harvest
        self.natural_gift_power = natural_gift_power
        self.size = size
        self.smoothness = smoothness
        self.soil_dryness = soil_dryness
        self.firmness = NamedAPIResource(**firmness)
        self.flavors = (
            [BerryFlavorMap(**flavor) for flavor in flavors] if flavors else []
        )
        self.item = NamedAPIResource(**item)
        self.natural_gift_type = NamedAPIResource(**natural_gift_type)

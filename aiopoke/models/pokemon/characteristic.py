from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.stats import Stat
from aiopoke.models.utility.common_model import Description, NamedAPIResource


@dataclass
class Characteristic:
    id: int
    gene_modulo: int
    possible_values: List[int]
    highest_stat: "NamedAPIResource[Stat]"
    descriptions: List["Description"]

    def __init__(
        self,
        *,
        id: int,
        gene_modulo: int,
        possible_values: List[int],
        highest_stat: Dict[str, Any],
        descriptions: List[Dict[str, Any]],
    ) -> None:
        self.id = id
        self.gene_modulo = gene_modulo
        self.possible_values = possible_values
        self.highest_stat = NamedAPIResource(**highest_stat)
        self.descriptions = (
            [Description(**description) for description in descriptions]
            if descriptions
            else []
        )

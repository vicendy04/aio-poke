from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from aiopoke.models.pokemon.stats import Stat
from aiopoke.models.utility.common_model import Description, NamedAPIResource


class Characteristic:
    id: int
    gene_modulo: int
    possible_values: List[int]
    highest_stat: "NamedAPIResource[Stat]"
    descriptions: List["Description"]

from typing import List

from aiopoke.models.pokemon.stats import Stat
from aiopoke.models.utility.common_model import NamedAPIResource, Description


class Characteristic:
    id: int
    gene_modulo: int
    possible_values: List[int]
    highest_stat: NamedAPIResource[Stat]
    descriptions: List["Description"]

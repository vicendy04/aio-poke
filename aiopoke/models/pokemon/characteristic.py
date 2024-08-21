from typing import List

from aiopoke.models.utility.common_models import AdditionalResource, Description


class Characteristic:
    id: int
    gene_modulo: int
    possible_values: List[int]
    highest_stat: AdditionalResource
    descriptions: List["Description"]

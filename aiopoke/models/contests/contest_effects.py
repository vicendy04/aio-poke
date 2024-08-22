from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_model import Effect, FlavorText


@dataclass
class ContestEffect:
    id: int
    appeal: int
    jam: int
    effect_entries: List[Effect]
    flavor_text_entries: List[FlavorText]

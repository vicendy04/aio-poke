from typing import List
from aiopoke.models.utility.common_models import AdditionalResource, FlavorText


class SuperContestEffect:
    id: int
    appeal: int
    flavor_text_entries: List["FlavorText"]
    moves: List[AdditionalResource]

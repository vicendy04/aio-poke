from typing import List
from aiopoke.models.moves.moves import Move
from aiopoke.models.utility.common_model import AdditionalResource, FlavorText


class SuperContestEffect:
    id: int
    appeal: int
    flavor_text_entries: List["FlavorText"]
    moves: List[AdditionalResource[Move]]

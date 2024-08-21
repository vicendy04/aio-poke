from dataclasses import dataclass

from aiopoke.models.utility.common_models import AdditionalResource, CommonResource


@dataclass
class VersionGroup(CommonResource):
    order: int
    generation: AdditionalResource
    move_learn_methods: AdditionalResource
    pokedexes: AdditionalResource
    regions: AdditionalResource
    versions: AdditionalResource

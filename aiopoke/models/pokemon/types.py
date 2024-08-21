from dataclasses import dataclass
from typing import List

from aiopoke.models.utility.common_models import (
    AdditionalResource,
    CommonResource,
    GenerationGameIndex,
    Name,
)


@dataclass
class TypeRelations:
    no_damage_to: List[AdditionalResource]
    half_damage_to: List[AdditionalResource]
    double_damage_to: List[AdditionalResource]
    no_damage_from: List[AdditionalResource]
    half_damage_from: List[AdditionalResource]
    double_damage_from: List[AdditionalResource]


@dataclass
class GameIndex:
    game_index: int
    generation: AdditionalResource


@dataclass
class PastDamageRelation:
    generation: AdditionalResource
    damage_relations: TypeRelations


@dataclass
class TypePokemon:
    slot: int
    pokemon: AdditionalResource


@dataclass
class TypeRelationsPast:
    generation: AdditionalResource
    damage_relations: TypeRelations


@dataclass
class Type(CommonResource):
    damage_relations: TypeRelations

    past_damage_relations: List[TypeRelationsPast]
    game_indices: List[GenerationGameIndex]

    generation: AdditionalResource
    move_damage_class: AdditionalResource

    names: List[Name]
    pokemon: List[TypePokemon]
    moves: List[AdditionalResource]

from dataclasses import dataclass
from typing import List

from aiopoke.models.games.generations import Generation
from aiopoke.models.moves.move_damage_classes import MoveDamageClass
from aiopoke.models.moves.moves import Move
from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.utility.common_model import (
    AdditionalResource,
    CommonResource,
    GenerationGameIndex,
    Name,
)


@dataclass
class TypeRelations:
    no_damage_to: List[AdditionalResource["Type"]]
    half_damage_to: List[AdditionalResource["Type"]]
    double_damage_to: List[AdditionalResource["Type"]]
    no_damage_from: List[AdditionalResource["Type"]]
    half_damage_from: List[AdditionalResource["Type"]]
    double_damage_from: List[AdditionalResource["Type"]]


@dataclass
class TypePokemon:
    slot: int
    pokemon: AdditionalResource[Pokemon]


@dataclass
class TypeRelationsPast:
    generation: AdditionalResource[Generation]
    damage_relations: TypeRelations


@dataclass
class Type(CommonResource):
    damage_relations: TypeRelations

    past_damage_relations: List[TypeRelationsPast]
    game_indices: List[GenerationGameIndex]

    generation: AdditionalResource[Generation]
    move_damage_class: AdditionalResource[MoveDamageClass]

    names: List[Name]
    pokemon: List[TypePokemon]
    moves: List[AdditionalResource[Move]]

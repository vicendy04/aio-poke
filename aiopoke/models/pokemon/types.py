from dataclasses import dataclass
from typing import List

from aiopoke.models.games.generations import Generation
from aiopoke.models.moves.move_damage_classes import MoveDamageClass
from aiopoke.models.moves.moves import Move
from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.utility.common_model import (
    NamedAPIResource,
    CommonResource,
    GenerationGameIndex,
    Name,
)


@dataclass
class TypeRelations:
    no_damage_to: List[NamedAPIResource["Type"]]
    half_damage_to: List[NamedAPIResource["Type"]]
    double_damage_to: List[NamedAPIResource["Type"]]
    no_damage_from: List[NamedAPIResource["Type"]]
    half_damage_from: List[NamedAPIResource["Type"]]
    double_damage_from: List[NamedAPIResource["Type"]]


@dataclass
class TypePokemon:
    slot: int
    pokemon: NamedAPIResource[Pokemon]


@dataclass
class TypeRelationsPast:
    generation: NamedAPIResource[Generation]
    damage_relations: TypeRelations


@dataclass
class Type(CommonResource):
    damage_relations: TypeRelations

    past_damage_relations: List[TypeRelationsPast]
    game_indices: List[GenerationGameIndex]

    generation: NamedAPIResource[Generation]
    move_damage_class: NamedAPIResource[MoveDamageClass]

    names: List[Name]
    pokemon: List[TypePokemon]
    moves: List[NamedAPIResource[Move]]

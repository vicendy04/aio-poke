from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from aiopoke.models.games.generations import Generation
    from aiopoke.models.moves.move_damage_classes import MoveDamageClass
    from aiopoke.models.moves.moves import Move
    from aiopoke.models.pokemon.pokemon import Pokemon
from aiopoke.models.utility.common_model import (
    CommonResource,
    GenerationGameIndex,
    Name,
    NamedAPIResource,
)


@dataclass
class TypeRelations:
    no_damage_to: List[NamedAPIResource["Type"]]
    half_damage_to: List[NamedAPIResource["Type"]]
    double_damage_to: List[NamedAPIResource["Type"]]
    no_damage_from: List[NamedAPIResource["Type"]]
    half_damage_from: List[NamedAPIResource["Type"]]
    double_damage_from: List[NamedAPIResource["Type"]]

    def __init__(
        self,
        *,
        no_damage_to: List[Dict[str, Any]],
        half_damage_to: List[Dict[str, Any]],
        double_damage_to: List[Dict[str, Any]],
        no_damage_from: List[Dict[str, Any]],
        half_damage_from: List[Dict[str, Any]],
        double_damage_from: List[Dict[str, Any]],
    ) -> None:
        self.no_damage_to = (
            [NamedAPIResource(**type_) for type_ in no_damage_to]
            if no_damage_to
            else []
        )
        self.half_damage_to = (
            [NamedAPIResource(**type_) for type_ in half_damage_to]
            if half_damage_to
            else []
        )
        self.double_damage_to = (
            [NamedAPIResource(**type_) for type_ in double_damage_to]
            if double_damage_to
            else []
        )
        self.no_damage_from = (
            [NamedAPIResource(**type_) for type_ in no_damage_from]
            if no_damage_from
            else []
        )
        self.half_damage_from = (
            [NamedAPIResource(**type_) for type_ in half_damage_from]
            if half_damage_from
            else []
        )
        self.double_damage_from = (
            [NamedAPIResource(**type_) for type_ in double_damage_from]
            if double_damage_from
            else []
        )


@dataclass
class TypePokemon:
    slot: int
    pokemon: NamedAPIResource["Pokemon"]

    def __init__(
        self,
        *,
        slot: int,
        pokemon: Dict[str, Any],
    ) -> None:
        self.slot = slot
        self.pokemon = NamedAPIResource(**pokemon)


@dataclass
class TypeRelationsPast:
    generation: NamedAPIResource["Generation"]
    damage_relations: TypeRelations

    def __init__(
        self,
        *,
        generation: Dict[str, Any],
        damage_relations: Dict[str, Any],
    ) -> None:
        self.generation = NamedAPIResource(**generation)
        self.damage_relations = TypeRelations(**damage_relations)


@dataclass
class Type(CommonResource):
    damage_relations: TypeRelations
    past_damage_relations: List[TypeRelationsPast]
    game_indices: List["GenerationGameIndex"]
    generation: NamedAPIResource["Generation"]
    move_damage_class: NamedAPIResource["MoveDamageClass"]
    names: List["Name"]
    pokemon: List[TypePokemon]
    moves: List[NamedAPIResource["Move"]]

    def __init__(
        self,
        *,
        id: int,
        name: str,
        damage_relations: Dict[str, Any],
        past_damage_relations: List[Dict[str, Any]],
        game_indices: List[Dict[str, Any]],
        generation: Dict[str, Any],
        move_damage_class: Dict[str, Any],
        names: List[Dict[str, Any]],
        pokemon: List[Dict[str, Any]],
        moves: List[Dict[str, Any]],
    ) -> None:
        super().__init__(id=id, name=name)
        self.damage_relations = TypeRelations(**damage_relations)
        self.past_damage_relations = (
            [
                TypeRelationsPast(**past_relation)
                for past_relation in past_damage_relations
            ]
            if past_damage_relations
            else []
        )
        self.game_indices = (
            [GenerationGameIndex(**index) for index in game_indices]
            if game_indices
            else []
        )
        self.generation = NamedAPIResource(**generation)
        self.move_damage_class = NamedAPIResource(**move_damage_class)
        self.names = [Name(**name) for name in names] if names else []
        self.pokemon = (
            [TypePokemon(**pokemon) for pokemon in pokemon] if pokemon else []
        )
        self.moves = [NamedAPIResource(**move) for move in moves] if moves else []

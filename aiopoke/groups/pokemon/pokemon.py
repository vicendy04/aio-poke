from dataclasses import dataclass
from typing import List, Dict, Optional

from aiopoke.groups.utility.common_models import IdentifiedResource


@dataclass
class Species:
    name: str
    url: str


@dataclass
class Ability:
    is_hidden: bool
    slot: int
    ability: Species


@dataclass
class Cries:
    latest: str
    legacy: str


@dataclass
class GameIndex:
    game_index: int
    version: Species


@dataclass
class VersionDetail:
    rarity: int
    version: Species


@dataclass
class HeldItem:
    item: Species
    version_details: List[VersionDetail]


@dataclass
class VersionGroupDetail:
    level_learned_at: int
    version_group: Species
    move_learn_method: Species


@dataclass
class Move:
    move: Species
    version_group_details: List[VersionGroupDetail]


@dataclass
class TypeElement:
    slot: int
    type: Species


@dataclass
class PastType:
    generation: Species
    types: List[TypeElement]


@dataclass
class RedBlue:
    back_default: str
    back_gray: str
    front_default: str
    front_gray: str


@dataclass
class GenerationI:
    red_blue: RedBlue
    yellow: RedBlue


@dataclass
class Crystal:
    back_default: str
    back_shiny: str
    front_default: str
    front_shiny: str


@dataclass
class GenerationIi:
    crystal: Crystal
    gold: Crystal
    silver: Crystal


@dataclass
class OfficialArtwork:
    front_default: str
    front_shiny: str


@dataclass
class GenerationIii:
    emerald: OfficialArtwork
    firered_leafgreen: Crystal
    ruby_sapphire: Crystal


@dataclass
class Home:
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None


@dataclass
class DreamWorld:
    front_default: str
    front_female: None


@dataclass
class GenerationVii:
    icons: DreamWorld
    ultra_sun_ultra_moon: Home


@dataclass
class GenerationViii:
    icons: DreamWorld


@dataclass
class GenerationV:
    black_white: "Sprites"


@dataclass
class GenerationIv:
    diamond_pearl: "Sprites"
    heartgold_soulsilver: "Sprites"
    platinum: "Sprites"


@dataclass
class Versions:
    generation_i: GenerationI
    generation_ii: GenerationIi
    generation_iii: GenerationIii
    generation_iv: GenerationIv
    generation_v: GenerationV
    generation_vi: Dict[str, Home]
    generation_vii: GenerationVii
    generation_viii: GenerationViii


@dataclass
class Other:
    dream_world: DreamWorld
    home: Home
    official_artwork: OfficialArtwork
    showdown: "Sprites"


@dataclass
class Sprites:
    back_default: str
    back_female: None
    back_shiny: str
    back_shiny_female: None
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None
    other: Optional[Other] = None
    versions: Optional[Versions] = None
    animated: Optional["Sprites"] = None


@dataclass
class Stat:
    base_stat: int
    effort: int
    stat: Species


@dataclass
class Pokemon(IdentifiedResource):
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[Ability]
    forms: List[Species]
    game_indices: List[GameIndex]
    held_items: List[HeldItem]
    location_area_encounters: str
    moves: List[Move]
    species: Species
    sprites: Sprites
    cries: Cries
    stats: List[Stat]
    types: List[TypeElement]
    past_types: List[PastType]

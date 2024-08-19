from typing import List, Dict, Optional


class Species:
    name: str
    url: str

    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self.url = url


class PokemonAbility:
    is_hidden: bool
    slot: int
    # here
    ability: Species

    def __init__(self, is_hidden: bool, slot: int, ability: Species) -> None:
        self.is_hidden = is_hidden
        self.slot = slot
        self.ability = ability


class PokemonCries:
    latest: str
    legacy: str

    def __init__(self, latest: str, legacy: str) -> None:
        self.latest = latest
        self.legacy = legacy


class GameIndex:
    game_index: int
    version: Species

    def __init__(self, game_index: int, version: Species) -> None:
        self.game_index = game_index
        self.version = version


class PokemonHeldItemVersion:
    # here
    version: Species
    rarity: int

    def __init__(self, rarity: int, version: Species) -> None:
        self.rarity = rarity
        self.version = version


class PokemonHeldItem:
    # here
    item: Species
    version_details: List[PokemonHeldItemVersion]

    def __init__(
        self, item: Species, version_details: List[PokemonHeldItemVersion]
    ) -> None:
        self.item = item
        self.version_details = version_details


class PokemonMoveVersion:
    level_learned_at: int
    # here
    version_group: Species
    move_learn_method: Species

    def __init__(
        self, level_learned_at: int, version_group: Species, move_learn_method: Species
    ) -> None:
        self.level_learned_at = level_learned_at
        self.version_group = version_group
        self.move_learn_method = move_learn_method


class PokemonMove:
    # here
    move: Species
    # here
    version_group_details: List[PokemonMoveVersion]

    def __init__(
        self, move: Species, version_group_details: List[PokemonMoveVersion]
    ) -> None:
        self.move = move
        self.version_group_details = version_group_details


class PokemonType:
    slot: int
    # here
    type: Species

    def __init__(self, slot: int, type: Species) -> None:
        self.slot = slot
        self.type = type


class PokemonTypePast:
    # here
    generation: Species
    types: List[PokemonType]

    def __init__(self, generation: Species, types: List[PokemonType]) -> None:
        self.generation = generation
        self.types = types


class RedBlue:
    back_default: str
    back_gray: str
    front_default: str
    front_gray: str

    def __init__(
        self, back_default: str, back_gray: str, front_default: str, front_gray: str
    ) -> None:
        self.back_default = back_default
        self.back_gray = back_gray
        self.front_default = front_default
        self.front_gray = front_gray


class GenerationI:
    red_blue: RedBlue
    yellow: RedBlue

    def __init__(self, red_blue: RedBlue, yellow: RedBlue) -> None:
        self.red_blue = red_blue
        self.yellow = yellow


class Crystal:
    back_default: str
    back_shiny: str
    front_default: str
    front_shiny: str

    def __init__(
        self, back_default: str, back_shiny: str, front_default: str, front_shiny: str
    ) -> None:
        self.back_default = back_default
        self.back_shiny = back_shiny
        self.front_default = front_default
        self.front_shiny = front_shiny


class GenerationIi:
    crystal: Crystal
    gold: Crystal
    silver: Crystal

    def __init__(self, crystal: Crystal, gold: Crystal, silver: Crystal) -> None:
        self.crystal = crystal
        self.gold = gold
        self.silver = silver


class OfficialArtwork:
    front_default: str
    front_shiny: str

    def __init__(self, front_default: str, front_shiny: str) -> None:
        self.front_default = front_default
        self.front_shiny = front_shiny


class GenerationIii:
    emerald: OfficialArtwork
    firered_leafgreen: Crystal
    ruby_sapphire: Crystal

    def __init__(
        self,
        emerald: OfficialArtwork,
        firered_leafgreen: Crystal,
        ruby_sapphire: Crystal,
    ) -> None:
        self.emerald = emerald
        self.firered_leafgreen = firered_leafgreen
        self.ruby_sapphire = ruby_sapphire


class Home:
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None

    def __init__(
        self,
        front_default: str,
        front_female: None,
        front_shiny: str,
        front_shiny_female: None,
    ) -> None:
        self.front_default = front_default
        self.front_female = front_female
        self.front_shiny = front_shiny
        self.front_shiny_female = front_shiny_female


class DreamWorld:
    front_default: str
    front_female: None

    def __init__(self, front_default: str, front_female: None) -> None:
        self.front_default = front_default
        self.front_female = front_female


class GenerationVii:
    icons: DreamWorld
    ultra_sun_ultra_moon: Home

    def __init__(self, icons: DreamWorld, ultra_sun_ultra_moon: Home) -> None:
        self.icons = icons
        self.ultra_sun_ultra_moon = ultra_sun_ultra_moon


class GenerationViii:
    icons: DreamWorld

    def __init__(self, icons: DreamWorld) -> None:
        self.icons = icons


class GenerationV:
    black_white: "PokemonSprites"

    def __init__(self, black_white: "PokemonSprites") -> None:
        self.black_white = black_white


class GenerationIv:
    diamond_pearl: "PokemonSprites"
    heartgold_soulsilver: "PokemonSprites"
    platinum: "PokemonSprites"

    def __init__(
        self,
        diamond_pearl: "PokemonSprites",
        heartgold_soulsilver: "PokemonSprites",
        platinum: "PokemonSprites",
    ) -> None:
        self.diamond_pearl = diamond_pearl
        self.heartgold_soulsilver = heartgold_soulsilver
        self.platinum = platinum


class Versions:
    generation_i: GenerationI
    generation_ii: GenerationIi
    generation_iii: GenerationIii
    generation_iv: GenerationIv
    generation_v: GenerationV
    generation_vi: Dict[str, Home]
    generation_vii: GenerationVii
    generation_viii: GenerationViii

    def __init__(
        self,
        generation_i: GenerationI,
        generation_ii: GenerationIi,
        generation_iii: GenerationIii,
        generation_iv: GenerationIv,
        generation_v: GenerationV,
        generation_vi: Dict[str, Home],
        generation_vii: GenerationVii,
        generation_viii: GenerationViii,
    ) -> None:
        self.generation_i = generation_i
        self.generation_ii = generation_ii
        self.generation_iii = generation_iii
        self.generation_iv = generation_iv
        self.generation_v = generation_v
        self.generation_vi = generation_vi
        self.generation_vii = generation_vii
        self.generation_viii = generation_viii


class Other:
    dream_world: DreamWorld
    home: Home
    official_artwork: OfficialArtwork
    showdown: "PokemonSprites"

    def __init__(
        self,
        dream_world: DreamWorld,
        home: Home,
        official_artwork: OfficialArtwork,
        showdown: "PokemonSprites",
    ) -> None:
        self.dream_world = dream_world
        self.home = home
        self.official_artwork = official_artwork
        self.showdown = showdown


class PokemonSprites:
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None
    back_default: str
    back_female: None
    back_shiny: str
    back_shiny_female: None
    # Option[X] == Union[X, None]
    # here
    other: Optional[Other]
    versions: Optional[Versions]
    animated: Optional["PokemonSprites"]

    def __init__(
        self,
        back_default: str,
        back_female: None,
        back_shiny: str,
        back_shiny_female: None,
        front_default: str,
        front_female: None,
        front_shiny: str,
        front_shiny_female: None,
        other: Optional[Other],
        versions: Optional[Versions],
        animated: Optional["PokemonSprites"],
    ) -> None:
        self.back_default = back_default
        self.back_female = back_female
        self.back_shiny = back_shiny
        self.back_shiny_female = back_shiny_female
        self.front_default = front_default
        self.front_female = front_female
        self.front_shiny = front_shiny
        self.front_shiny_female = front_shiny_female
        self.other = other
        self.versions = versions
        self.animated = animated


class PokemonStat:
    base_stat: int
    effort: int
    # here
    stat: Species

    def __init__(self, base_stat: int, effort: int, stat: Species) -> None:
        self.base_stat = base_stat
        self.effort = effort
        self.stat = stat


class Pokemon:
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int

    abilities: List[PokemonAbility]
    forms: List[Species]
    game_indices: List[GameIndex]
    held_items: List[PokemonHeldItem]
    location_area_encounters: str

    moves: List[PokemonMove]

    species: Species
    sprites: PokemonSprites
    cries: PokemonCries

    stats: List[PokemonStat]
    types: List[PokemonType]
    past_types: List[PokemonTypePast]

    def __init__(
        self,
        id: int,
        name: str,
        base_experience: int,
        height: int,
        is_default: bool,
        order: int,
        weight: int,
        abilities: List[PokemonAbility],
        forms: List[Species],
        game_indices: List[GameIndex],
        held_items: List[PokemonHeldItem],
        location_area_encounters: str,
        moves: List[PokemonMove],
        species: Species,
        sprites: PokemonSprites,
        cries: PokemonCries,
        stats: List[PokemonStat],
        types: List[PokemonType],
        past_types: List[PokemonTypePast],
    ) -> None:
        self.id = id
        self.name = name
        self.base_experience = base_experience
        self.height = height
        self.is_default = is_default
        self.order = order
        self.weight = weight
        self.abilities = abilities
        self.forms = forms
        self.game_indices = game_indices
        self.held_items = held_items
        self.location_area_encounters = location_area_encounters
        self.moves = moves
        self.species = species
        self.sprites = sprites
        self.cries = cries
        self.stats = stats
        self.types = types
        self.past_types = past_types

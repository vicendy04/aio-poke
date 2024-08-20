import asyncio

from aiopoke.adaptor import RestAdapter
from aiopoke.groups.pokemon.pokemon import Pokemon
from aiopoke.service import PokeAPIService


async def print_language():
    poke_service = PokeAPIService()
    adapter = RestAdapter(service=poke_service)

    # Fetch language data
    pokemon_data = await adapter.get_pokemon(1)
    # Object
    pokemon = Pokemon(**pokemon_data)

    # Print the result
    # print(language)
    print("--------------------------")
    print(pokemon.id)
    print(pokemon.name)
    print(pokemon.base_experience)
    print(pokemon.moves[0].move.name)
    print(pokemon.moves[0].move.url)
    print("--------------------------")


asyncio.run(print_language())

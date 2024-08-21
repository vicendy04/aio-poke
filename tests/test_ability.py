import asyncio
from aiopoke.adaptor import PokeAPIClient
from aiopoke.service import PokeAPIService


async def print_ability():
    poke_service = PokeAPIService()
    adapter = PokeAPIClient(service=poke_service)

    ability_data = await adapter.get_ability("overgrow")
    print("Result for 'overgrow':", ability_data)

    ability_data = await adapter.get_ability("blaze")
    print("Result for 'blaze':", ability_data)


asyncio.run(print_ability())

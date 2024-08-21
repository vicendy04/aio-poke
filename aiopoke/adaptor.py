from typing import Any, Dict

from aiopoke.service import PokeAPIService


class PokeAPIClient:
    def __init__(self, service: PokeAPIService):
        self.service = service

    async def get_ability(self, identifier: Any) -> Dict:
        endpoint = f"ability/{identifier}"
        data = await self.service.get(endpoint)
        return data

    async def get_language(self, identifier: Any) -> Dict:
        endpoint = f"language/{identifier}"
        data = await self.service.get(endpoint)
        return data

    async def get_pokemon(self, identifier: Any) -> Dict:
        endpoint = f"pokemon/{identifier}"
        data = await self.service.get(endpoint)
        return data

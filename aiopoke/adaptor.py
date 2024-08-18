from typing import Any, Dict

from aiopoke.service import PokeAPIService


class RestAdapter:
    def __init__(self, service: PokeAPIService):
        self.service = service

    async def get_ability(self, identifier: Any) -> Dict:
        endpoint = f"ability/{identifier}"
        data = await self.service.get(endpoint)
        return data

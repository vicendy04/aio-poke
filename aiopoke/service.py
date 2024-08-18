from typing import Any, Dict
import aiohttp


class PokeAPIService:
    BASE_URL: str = "https://pokeapi.co/api/v2/"

    def __init__(self) -> None:
        pass

    async def get(self, endpoint: str) -> Dict[str, Any]:
        full_url = self.BASE_URL + endpoint
        async with aiohttp.ClientSession() as session:
            async with session.get(full_url) as response:
                if response.status == 200:
                    return await response.json()
                try:
                    error_data = await response.json()
                    error_message = error_data.get("message", "Unknown error occurred")
                except Exception:
                    error_message = "Unknown error occurred"
                raise Exception(f"HTTP Error {response.status}: {error_message}")

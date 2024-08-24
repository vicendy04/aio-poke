from typing import Any, Dict

import aiohttp


class PokeAPIService:
    BASE_URL: str = "https://pokeapi.co/api/v2/"

    def __init__(self) -> None:
        pass

    async def get(self, endpoint: str) -> Dict[str, Any]:
        full_url = self.BASE_URL + endpoint
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(full_url) as response:
                    # Raise ``Exception`` if ``status`` is more than ``400``.
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientResponseError as e:
            error_message = f"HTTP Error: {e.status} - {e.message}"
            raise Exception(error_message) from e
        except aiohttp.ClientError as e:
            raise Exception("Failed to connect to the API.") from e
        except Exception as e:
            raise Exception("An unexpected error occurred.") from e

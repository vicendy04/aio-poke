import asyncio
import json

from aiopoke.adaptor import RestAdapter
from aiopoke.groups.utility.languages import Language
from aiopoke.service import PokeAPIService

json_str = """
{
  "id": 1,
  "name": "ja",
  "official": true,
  "iso639": "ja",
  "iso3166": "jp",
  "names": [
    {
      "name": "Japanese",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      }
    }
  ]
}
"""


async def print_language():
    poke_service = PokeAPIService()
    adapter = RestAdapter(service=poke_service)

    # Fetch language data
    language_data = await adapter.get_language(1)
    # Object
    language = Language(**language_data)

    # Print the result
    print(language)
    print("--------------------------")
    print(language.id)
    print(language.name)
    print(language.official)
    print(language.iso3166)
    print(language.iso639)
    print("--------------------------")
    first_name = language.names[0]
    print(first_name)
    print(first_name.language.name)  # bug here
    print(first_name.language.url)  # bug here
    print(type(language.names))


asyncio.run(print_language())

import json

from aiopoke.groups.utility.languages import Language

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

# Parse JSON string
data = json.loads(json_str)

language = Language(**data)

# Print the result
print(language)
print("--------------------------")
print(language.id)
print(language.name)
print(language.official)
print(language.iso3166)
print(language.iso639)
print(language.names)
print(type(language.names))

import json
from pathlib import Path

number = int(input("Apa angka favoritmu? "))

path = Path(__file__).parent / 'favorite_number.json'
contents = json.dumps(number)
path.write_text(contents)

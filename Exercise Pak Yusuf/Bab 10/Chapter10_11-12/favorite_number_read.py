import json
from pathlib import Path

path = Path(__file__).parent / 'favorite_number.json'
contents = path.read_text()
number = json.loads(contents)

print(f"Aku tahu angka favoritmu! Yaitu {number}.")

import json
from pathlib import Path

path = Path(__file__).parent / 'favorite_number.json'

if path.exists():
    # Angka sudah tersimpan: baca dan tampilkan
    contents = path.read_text()
    number = json.loads(contents)
    print(f"Aku tahu angka favoritmu! Yaitu {number}.")
else:
    # Belum ada: tanya dulu, lalu simpan
    number = int(input("Apa angka favoritmu? "))
    contents = json.dumps(number)
    path.write_text(contents)
    print("Oke, angka favoritmu sudah kuingat!")
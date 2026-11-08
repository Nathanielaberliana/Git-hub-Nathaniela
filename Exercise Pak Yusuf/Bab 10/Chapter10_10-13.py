import json
from pathlib import Path

path = Path(__file__).parent / 'user_info.json'

# Kalau data belum tersimpan, tanya dulu lalu simpan sebagai dictionary
if not path.exists():
    username = input("Siapa namamu? ")
    city = input("Kamu tinggal di kota mana? ")
    hobby = input("Apa hobimu? ")

    user_info = {
        'username': username,
        'city': city,
        'hobby': hobby,
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    print("\nOke, datamu sudah kuingat!")

# Baca kembali data dari file dan tampilkan ringkasannya
contents = path.read_text()
user_info = json.loads(contents)

print("\nIni yang kuingat tentang kamu:")
print(f"Nama: {user_info['username'].title()}")
print(f"Kota: {user_info['city'].title()}")
print(f"Hobi: {user_info['hobby']}")

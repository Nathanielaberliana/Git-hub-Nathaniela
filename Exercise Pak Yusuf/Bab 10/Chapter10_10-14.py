import json
from pathlib import Path


def get_stored_username(path):
    """Ambil nama pengguna yang tersimpan, kalau ada."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Tanya nama pengguna baru dan simpan ke file."""
    username = input("Siapa namamu? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Sapa pengguna dengan namanya, setelah memastikan namanya benar."""
    path = Path(__file__).parent / 'username.json'
    username = get_stored_username(path)

    if username:
        correct = input(f"Apakah kamu {username}? ")
        if correct == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingatmu, {username}!")
    else:
        username = get_new_username(path)
        print(f"Kami akan mengingatmu, {username}!")


greet_user()


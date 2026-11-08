from pathlib import Path

names = []

while True:
    name = input("Siapa namamu? (ketik 'q' untuk selesai) ")
    if name == 'q':
        break

    names.append(name)
    print(f"Halo {name}, namamu sudah dicatat!")

path = Path(__file__).parent / 'guest_book.txt'
path.write_text("\n".join(names))


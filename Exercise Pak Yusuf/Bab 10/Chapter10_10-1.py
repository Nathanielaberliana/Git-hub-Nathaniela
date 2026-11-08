from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'

# Cara 1: baca seluruh isi file sekaligus
print("Cara 1: membaca seluruh file")
contents = path.read_text()
print(contents)

# Cara 2: simpan baris-baris ke dalam list, lalu loop
print("Cara 2: membaca baris per baris")
lines = contents.splitlines()
for line in lines:
    print(line)
    
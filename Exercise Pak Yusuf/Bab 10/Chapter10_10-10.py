from pathlib import Path

filenames = ['cerita.txt']

for filename in filenames:
    path = Path(__file__).parent / filename

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Mohon maaf, file {filename} tidak ditemukan.")
    else:
        text = contents.lower()
        count_the = text.count('the')
        count_the_space = text.count('the ')

        print(f"\n{filename}:")
        print(f"  'the'  muncul {count_the:,} kali.")
        print(f"  'the ' muncul {count_the_space:,} kali.")
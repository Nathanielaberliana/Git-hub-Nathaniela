from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    modified_line = line.replace('Python', 'C')
    print(modified_line)
    
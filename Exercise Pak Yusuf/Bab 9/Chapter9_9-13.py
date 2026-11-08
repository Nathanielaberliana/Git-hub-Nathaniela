from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Cetak angka acak antara 1 dan jumlah sisi dadu."""
        print(randint(1, self.sides))


d6 = Die()
print("Dadu 6 sisi:")
for roll_num in range(10):
    d6.roll_die()

d10 = Die(10)
print("\nDadu 10 sisi:")
for roll_num in range(10):
    d10.roll_die()

d20 = Die(20)
print("\nDadu 20 sisi:")
for roll_num in range(10):
    d20.roll_die()
    
    
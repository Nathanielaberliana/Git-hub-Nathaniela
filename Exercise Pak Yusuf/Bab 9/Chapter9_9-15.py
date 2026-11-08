from random import choice

items = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')

my_ticket = [3, 'a', 7, 'c']
print(f"Tiket saya: {my_ticket}")

attempts = 0
while True:
    attempts += 1

    # Undi tiket pemenang baru (empat item berbeda)
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(items)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    # Berhenti kalau tiket pemenang sama persis dengan tiket saya
    if winning_ticket == my_ticket:
        break

print(f"Tiket saya menang setelah {attempts:,} kali undian.")
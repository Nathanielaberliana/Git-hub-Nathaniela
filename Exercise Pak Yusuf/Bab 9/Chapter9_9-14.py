from random import choice

items = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')

winning_ticket = []

while len(winning_ticket) < 4:
    pulled_item = choice(items)

    # Pastikan item yang sama tidak terambil dua kali
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print("Tiket yang cocok dengan empat angka atau huruf berikut menang hadiah:")
for item in winning_ticket:
    print(item)
    
    
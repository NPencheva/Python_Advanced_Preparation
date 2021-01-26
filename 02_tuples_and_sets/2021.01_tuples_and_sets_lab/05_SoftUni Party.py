number_of_guests = int(input())
reservations = set()
visited_reservations = set()

for _ in range(number_of_guests):
    guest = input()
    reservations.add(guest)

command = input()

while not command == "END":
    visited_reservations.add(command)

    command = input()

guests_who_didnt_visit = sorted(reservations - visited_reservations)

print(len(guests_who_didnt_visit))

for g in guests_who_didnt_visit:
    print(g)

number_of_commands = int(input())
cars_in_parking_lot = set()

for _ in range(number_of_commands):
    action, car_number = input().split(", ")
    if action == "IN":
        cars_in_parking_lot.add(car_number)
    elif action == "OUT":
        cars_in_parking_lot.remove(car_number)

if cars_in_parking_lot:
    for car in cars_in_parking_lot:
        print(car)
else:
    print(f"Parking Lot is Empty")
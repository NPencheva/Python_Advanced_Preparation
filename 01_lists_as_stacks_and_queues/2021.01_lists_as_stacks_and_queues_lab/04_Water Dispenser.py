from collections import deque
starting_quantity = int(input())
queue = deque()
name_command = input()

while not name_command == "Start":
    queue.append(name_command)

    name_command = input()

command_line = input()

while not command_line == "End":
    command = command_line.split()
    if command[0] == "refill":
        liters = int(command[1])
        starting_quantity += liters
    else:
        liters = int(command[0])
        if liters > starting_quantity:
            print(f"{queue.popleft()} must wait")
        else:
            print(f"{queue.popleft()} got water")
            starting_quantity -= liters

    command_line = input()

print(f"{starting_quantity} liters left")
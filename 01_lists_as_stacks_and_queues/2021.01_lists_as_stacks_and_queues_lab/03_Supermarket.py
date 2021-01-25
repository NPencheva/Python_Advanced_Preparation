from collections import deque
command = input()
queue = deque()

while not command == "End":
    if command != "Paid":
        queue.append(command)
    else:
        while queue:
            print(queue[0])
            queue.popleft()

    command = input()

print(f"{len(queue)} people remaining.")
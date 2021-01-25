from collections import deque

kids = deque(input().split())
step_size = int(input())
counter = 0

while kids:
    counter += 1
    if counter % step_size != 0:
        kids.append(kids.popleft())
    else:
        if len(kids) == 1:
            print(f"Last is {kids.popleft()}")
        else:
            print(f"Removed {kids.popleft()}")
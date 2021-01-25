from collections import deque

food_quantity = int(input())
# food_queue_list = input().split()
#
# food_queue = deque(int(el) for el in food_queue_list)
food_queue = deque(int(el) for el in input().split())

print(max(food_queue))

while food_queue:
    if food_quantity >= food_queue[0]:
        food_quantity -= food_queue[0]
        food_queue.popleft()
    else:
        print(f"Orders left: ", end="")
        orders_left = [str(el) for el in food_queue]
        print(" ".join(orders_left))
        break

if not food_queue:
    print(f"Orders complete")
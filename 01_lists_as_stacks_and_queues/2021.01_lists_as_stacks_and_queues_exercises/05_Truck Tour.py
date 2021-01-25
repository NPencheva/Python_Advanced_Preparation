from collections import deque
number_of_pumps = int(input())
petrol_amount_deque = deque()
kilometers_deque = deque()
starting_index = 0
current_petrol = 0

for _ in range(number_of_pumps):
    petrol_amount, kilometers = input().split()
    petrol_amount_deque.append(int(petrol_amount))
    kilometers_deque.append(int(kilometers))

print(petrol_amount_deque)
print(kilometers_deque)

for index in range(number_of_pumps):
    current_petrol += petrol_amount_deque[index]
    if current_petrol >= kilometers_deque[index]:
        starting_index = index
    else:
        petrol_amount_deque.append(petrol_amount_deque.popleft())
        kilometers_deque.append(kilometers_deque.popleft())

print(petrol_amount_deque)
print(kilometers_deque)
print(starting_index)

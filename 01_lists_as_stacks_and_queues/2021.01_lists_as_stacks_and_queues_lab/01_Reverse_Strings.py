# https://judge.softuni.bg/Contests/1830

text = list(input())
new_string = []

for n in range(len(text)):
    # popped_item = text.pop()
    # new_string.append(popped_item)
    new_string.append(text.pop())

print("".join(new_string))
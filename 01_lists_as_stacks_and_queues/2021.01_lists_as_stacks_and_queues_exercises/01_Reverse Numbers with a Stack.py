# https://judge.softuni.bg/Contests/1831

integers = input().split()
new_text = []

for n in range(len(integers)):
    new_text.append(integers.pop())

print(" ".join(new_text))
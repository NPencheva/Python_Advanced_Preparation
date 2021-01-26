number_of_lines = int(input())
longest_len = 0
longest_intersection = []

for _ in range(number_of_lines):
    command = input().split("-")
    first_range = list(map(int, command[0].split(",")))
    second_range = list(map(int, command[1].split(",")))
    first_set = set()
    second_set = set()

    for n in range(first_range[0], first_range[1] + 1):
        first_set.add(n)
    for m in range(second_range[0], second_range[1] + 1):
        second_set.add(m)

    intersection = first_set & second_set
    if len(intersection) > longest_len:
        longest_len = len(intersection)
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {longest_len}")

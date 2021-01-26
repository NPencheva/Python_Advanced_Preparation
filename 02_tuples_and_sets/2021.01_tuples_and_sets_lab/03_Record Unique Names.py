number_of_names = int(input())
names_set = set()

for _ in range(number_of_names):
    name = input()
    names_set.add(name)

for unique_name in names_set:
    print(unique_name)
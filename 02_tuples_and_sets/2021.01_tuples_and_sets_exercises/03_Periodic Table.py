number_of_lines = int(input())
unique_elements = set()
for _ in range(number_of_lines):
    elements = input().split()
    for el in elements:
        unique_elements.add(el)

for unique in unique_elements:
    print(unique)
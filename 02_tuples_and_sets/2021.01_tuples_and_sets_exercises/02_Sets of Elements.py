len_1, len_2 = list(map(int, (x for x in input().split())))
set_1 = set()
set_2 = set()

for n in range(len_1):
    el_1 = int(input())
    set_1.add(el_1)


for m in range(len_2):
    el_2 = int(input())
    set_2.add(el_2)

repeated_elements = set_1 & set_2
for el in repeated_elements:
    print(el)

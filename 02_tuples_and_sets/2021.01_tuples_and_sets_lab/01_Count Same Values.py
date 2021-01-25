numbers_list = input().split()
numbers_tuple = tuple(float(x) for x in numbers_list)
uniques = []

for n in numbers_tuple:
    if n not in uniques:
        uniques.append(n)
        print(f"{n} - {numbers_tuple.count(n)} times")



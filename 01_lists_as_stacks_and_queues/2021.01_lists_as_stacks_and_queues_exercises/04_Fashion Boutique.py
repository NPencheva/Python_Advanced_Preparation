clothes_list = [int(el) for el in input().split()]
rack_capacity = int(input())
filled_capacity = 0
number_of_racks = 1
sum_of_clothes = 0

while clothes_list:
    if clothes_list[-1] + filled_capacity < rack_capacity:
        filled_capacity += clothes_list.pop()
    elif clothes_list[-1] + filled_capacity == rack_capacity:
        clothes_list.pop()
        if clothes_list:
            number_of_racks += 1
            filled_capacity = 0
    elif clothes_list[-1] + filled_capacity > rack_capacity:
        number_of_racks += 1
        filled_capacity = clothes_list.pop()

print(number_of_racks)
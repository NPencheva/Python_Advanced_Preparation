number_of_names = int(input())
odd_numbers = set()
even_numbers = set()
final_result = []

for n in range(1, number_of_names + 1):
    name = input()
    sum_chars = 0
    for char in name:
        sum_chars += ord(char)
    sum_chars //= n

    if sum_chars % 2 == 0:
        even_numbers.add(sum_chars)
    else:
        odd_numbers.add(sum_chars)

sum_of_odds = sum(odd_numbers)
sum_of_evens = sum(even_numbers)

if sum_of_odds == sum_of_evens:
    final_result = odd_numbers | even_numbers
elif sum_of_odds > sum_of_evens:
    final_result = odd_numbers - even_numbers
elif sum_of_evens > sum_of_odds:
    final_result = odd_numbers ^ even_numbers

final_result_str = list(map(str, final_result))

print(", ".join(final_result_str))

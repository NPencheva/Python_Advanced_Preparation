size = int(input())

matrix = []
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for row_index in range(size):
    row = [int(x) for x in input().split()]
    matrix.append(row)

# primary diagonal - еднакви индекси за редове и колони:

for column_index in range(size):
    for row_index in range(size):
        if column_index == row_index:
            primary_diagonal_sum += matrix[row_index][column_index]

# secondary diagonal - отпред назад и отзад напред като индекси за редове и колони, сумата на двата индекса,
# е равна на size - 1:

for column_index in range(size):
    for row_index in range(size):
        if column_index + row_index == size - 1:
            secondary_diagonal_sum += matrix[row_index][column_index]

absolute_diagonal_sum = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(absolute_diagonal_sum)

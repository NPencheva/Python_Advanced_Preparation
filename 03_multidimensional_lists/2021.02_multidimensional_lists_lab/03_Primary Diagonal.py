size = int(input())

matrix = []
primary_diagonal_sum = 0

for row_index in range(size):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for column_index in range(size):
    for row_index in range(size):
        if column_index == row_index:
            primary_diagonal_sum += matrix[row_index][column_index]

print(primary_diagonal_sum)

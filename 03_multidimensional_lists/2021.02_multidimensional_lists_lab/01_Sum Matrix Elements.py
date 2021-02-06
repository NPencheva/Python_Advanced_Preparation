number_of_rows, number_of_columns = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = 0

for row_index in range(number_of_rows):
    row = [int(y) for y in input().split(", ")]
    matrix.append(row)

for index in matrix:
    matrix_sum += sum(index)

print(matrix_sum)
print(matrix)

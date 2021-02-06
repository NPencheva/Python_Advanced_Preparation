number_of_rows, number_of_columns = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = 0

for row_index in range(number_of_rows):
    row = [int(y) for y in input().split()]
    matrix.append(row)

for column_index in range(number_of_columns):
    column_sum = 0
    for row_index in range(number_of_rows):
        column_sum += matrix[row_index][column_index]
    print(column_sum)

number_of_rows, number_of_columns = [int(x) for x in input().split()]

matrix = []
squares_2x2_count = 0

for row_index in range(number_of_rows):
    row = [y for y in input().split()]
    matrix.append(row)

for row_index in range(number_of_rows - 1):
    for column_index in range(number_of_columns - 1):
        if matrix[row_index][column_index] == matrix[row_index][column_index + 1] == matrix[row_index + 1][
            column_index] == matrix[row_index + 1][column_index + 1]:
            squares_2x2_count += 1

print(squares_2x2_count)

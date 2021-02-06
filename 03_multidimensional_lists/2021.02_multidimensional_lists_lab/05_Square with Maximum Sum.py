from sys import maxsize

number_of_rows, number_of_columns = [int(x) for x in input().split(", ")]

matrix = []

for row_index in range(number_of_rows):
    row = [int(y) for y in input().split(", ")]
    matrix.append(row)

max_square_sum = -maxsize
starting_row = 0
starting_column = 0

for row_index in range(number_of_rows - 1):
    for column_index in range(number_of_columns - 1):
        square_sum = matrix[row_index][column_index] + matrix[row_index][column_index + 1] + matrix[row_index + 1][
            column_index] + matrix[row_index + 1][column_index + 1]
        if square_sum > max_square_sum:
            max_square_sum = square_sum
            starting_row = row_index
            starting_column = column_index
print(f"{matrix[starting_row][starting_column]} {matrix[starting_row][starting_column + 1]}")
print(f"{matrix[starting_row + 1][starting_column]} {matrix[starting_row + 1][starting_column + 1]}")
print(max_square_sum)


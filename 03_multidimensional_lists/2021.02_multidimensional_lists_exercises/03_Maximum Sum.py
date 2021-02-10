from sys import maxsize

number_of_rows, number_of_columns = [int(x) for x in input().split()]

matrix = []

for row_index in range(number_of_rows):
    row = [int(y) for y in input().split()]
    matrix.append(row)

max_3x3_square_sum = -maxsize
starting_row = 0
starting_column = 0

for row_index in range(number_of_rows - 2):
    for column_index in range(number_of_columns - 2):
        square_3x3_sum = (matrix[row_index][column_index]
                          + matrix[row_index][column_index + 1]
                          + matrix[row_index][column_index + 2]
                          + matrix[row_index + 1][column_index]
                          + matrix[row_index + 1][column_index + 1]
                          + matrix[row_index + 1][column_index + 2]
                          + matrix[row_index + 2][column_index]
                          + matrix[row_index + 2][column_index + 1]
                          + matrix[row_index + 2][column_index + 2]
                          )
        if square_3x3_sum > max_3x3_square_sum:
            max_3x3_square_sum = square_3x3_sum

            starting_row = row_index
            starting_column = column_index

print(f"Sum = {max_3x3_square_sum}")

matrix_3x3 = [matrix[starting_row][starting_column:starting_column + 3],
              matrix[starting_row + 1][starting_column:starting_column + 3],
              matrix[starting_row + 2][starting_column:starting_column + 3]]

for index in range(len(matrix_3x3)):
    row_str = [str(x) for x in matrix_3x3[index]]
    final_row = " ".join(row_str)
    print(final_row)

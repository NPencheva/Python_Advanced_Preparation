size = int(input())

matrix = []

for r in range(size):
    row = [x for x in input()]
    matrix.append(row)

searched_symbol = input()

symbol_row = 0
symbol_column = 0
is_found = False

for row_index in range(size):
    if is_found:
        break
    for column_index in range(size):
        if matrix[row_index][column_index] == searched_symbol:
            symbol_row = row_index
            symbol_column = column_index
            is_found = True
            break

if is_found:
    found_symbols = (symbol_row, symbol_column)
    print(found_symbols)
else:
    print(f"{searched_symbol} does not occur in the matrix")

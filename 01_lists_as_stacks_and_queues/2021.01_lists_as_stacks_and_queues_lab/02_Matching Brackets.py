expression = input()
brackets_index = []

for index, value in enumerate(expression):
    if value == "(":
        brackets_index.append(index)
    elif value == ")":
        starting_index = brackets_index.pop()
        print(expression[starting_index:index + 1])

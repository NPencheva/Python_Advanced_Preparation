number = int(input())
stack = []
query = ""

for n in range(number):
    command = input().split()
    query_num = int(command[0])
    if query_num == 1:
        query = "Push"
    elif query_num == 2:
        query = "Delete"
    elif query_num == 3:
        query = "Print_max"
    elif query_num == 4:
        query = "Print_min"

    if query == "Push":
        stack.append(int(command[1]))
    else:
        if stack:
            if query == "Delete":
                stack.pop()
            elif query == "Print_max":
                print(max(stack))
            elif query == "Print_min":
                print(min(stack))

new_stack = reversed(list(map(lambda el: str(el), stack)))
print(", ".join(new_stack))

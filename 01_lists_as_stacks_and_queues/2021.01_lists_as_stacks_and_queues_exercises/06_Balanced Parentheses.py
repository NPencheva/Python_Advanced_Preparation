from collections import deque

sequence = deque(input())

if len(sequence) % 2 != 0:
    print("NO")

else:
    while sequence:
        if (
                (sequence[0] == "(" and sequence[-1] == ")")
            or (sequence[0] == "{" and sequence[-1] == "}")
            or (sequence[0] == "[" and sequence[-1] == "]")
        ):
            sequence.popleft()
            sequence.pop()
        else:
            print("NO")
            break

if not sequence:
    print("YES")

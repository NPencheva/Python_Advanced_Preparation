number_of_grades = int(input())
students_data = {}

for _ in range(number_of_grades):
    command = input().split()
    student = command[0]
    grade = float(command[1])
    if student not in students_data.keys():
        students_data[student] = [grade]
    else:
        students_data[student].append(grade)

for students, grades in students_data.items():
    average_grade = sum(grades)/len(grades)

    print(f"{students} -> ", end="")
    for grade in grades:
        print(f"{grade:.2f} ", end="")
    print(f"(avg: {average_grade:.2f})")

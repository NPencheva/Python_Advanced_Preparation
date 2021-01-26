command = input()
phonebook = {}
while "-" in command:   # while ord(command[0]) not in range(48, 58)
    name, phone_number = command.split("-")
    phonebook[name] = phone_number

    command = input()

number = int(command)

for n in range(number):
    searched_name = input()
    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
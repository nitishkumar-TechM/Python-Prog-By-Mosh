# While Loops

number = 100

while number > 0:
    print(number)
    number = number // 2
    # number //= 2


command = ""

# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


while True:
    print("Infinte loop")
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

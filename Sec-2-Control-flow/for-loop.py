# For Loop

# print("Sending a message")
# print("Sending a message")
# print("Sending a message")
# print("Sending a message")


# range(start, end, step)

# for number in range(3):
#     print("Attempt", number + 1, (number + 1)*".")

# for number in range(1, 4):
#     print("Attempt", number, number * ".")


for number in range(1, 10, 2):
    print("Attempt", number, number * ".")


# ***********************************************************
print("*********************** For-Else ******************************")

successful = False

for num in range(3):
    print("Nitish Attempt", num)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# Nested Loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# LEC-11 Iterables

print(type(5))
print(type(range(4)))
# it returns a 'range' object which is iterable
# In python String and lists are also iterable

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# for item in shopping_cart:
#     print(item)
# we are going to develop our own custom object
# and make it iterable
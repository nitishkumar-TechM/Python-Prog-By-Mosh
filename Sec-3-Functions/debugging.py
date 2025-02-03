def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))

# First mark a breakpoint
# fn + f5 to run file in debug mode
# f10 to next step and f11 to go inside a function
# shift + f11 to immediately out of the function
# Shift f5 to exit
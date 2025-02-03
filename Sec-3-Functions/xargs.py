# * args => that takes number of arguments

# [2, 3, 4, 5] = Square bracket for List
# (2, 3, 4, 5) = Parenthesis for Tuple, these are iterable

def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
        # total *= number        
    return total


print(multiply(2, 3, 4, 6))
# multiply(2, 3, 4, 6)

# ** args

def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])


# save_user(1, 2, 3, 4)
save_user(id=1, name="John", age=23)

# {'id': 1, 'name': 'John', 'age': 23} =  Dictionary in Python key, value pair 
# When we use ** , we can multiple argument with key-value pair
# and Python will automatically package them in a Dictionary


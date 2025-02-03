def greet(first_name, last_name="ok"):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Nitish", "Kumar")
greet("John", "Smith")
print(greet("nitish "))
# 'None' is the return value of the greet()
# In python by default every function return 'None' value
# 'None' is a object which represents the absence of a value

# 1 - Perform a task
# 2 - Return a value

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Tech Mahindra")
print(message)
file = open("content.txt", "w")
file.write(message)


# Keyword Argument

def increment(number, by=1):
    return number + by


# result = increment(2, 1)
# print('result', result)

print(increment(2, by=1))

# Default Argument
print(increment(7))
# All the optional parameter will come after the required parameter
# def dummy_fun(x, y=3, z) is a wrong syntax




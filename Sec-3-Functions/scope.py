message = "a"    #global

def greet(name):
    global message
    message = "b"


# It is possible that mutilple funs and variable rely on this global
# variable if we accidently modify them, then this will affect application
# Thats why this the  bad practice to modify global varible inside a function


# def send_email(name):
#     message = "b"


greet("Nitish")
print(message)
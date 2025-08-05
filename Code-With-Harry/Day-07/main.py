#Operators

print(5+6)
print(15-6)
print(15*6)
print(15/6)  #gives Float value
print(15//6)  #gives int value Floor Division Operator

print(5%3)
print(5**3)   # 5^3 exponential operator

# Exercise
'''
Create a calculator capable of performing addition, subtraction, multiplication, and division operations on two numbers.
Your program should format the output in a readable manner!
'''

print("Enter First Number :")
a = int(input())

print("Enter Second Number :")
b = int(input())

def sum(a,b):
    return a+b
    
def subtraction(a,b):
    return a-b
    
def multiplication(a,b):
    return a * b
    
def division(a,b):
    return a / b
    
print('Sum: ',sum(a,b))
print('Subtraction: ', subtraction(a,b))
print('Multiplication: ',multiplication(a,b))
print('Division: ', division(a,b))
    

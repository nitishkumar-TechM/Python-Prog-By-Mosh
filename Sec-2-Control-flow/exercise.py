# print even numbers between two numbers

x = int(input("Enter First range: "))
y = int(input("Enter End range: "))

count = 0
for num in range(x, y):
    if num % 2 == 0:
        count += 1
        print(num)

print(f"We have {count} even number")
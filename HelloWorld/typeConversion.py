# Type Conversion

x = input("x: ")
print(type(x))
y = int(x) + 1   # "1" + 1
print(y)
print(f"x: {x}, y:{y}")

# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy value in Python
# "" => empty string
# 0 => False
# None => Absence of value

# Any thing other than that is treated as Truthy value
#  bool("False") => True
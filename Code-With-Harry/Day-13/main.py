# String Methods

# Strings are immutable

a = "!!!!Nitish!!!!!!!"

print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))

b = "!!!!Nitish!!!!!!!Nitish!!!!!!"
print(b.replace("Nitish", "Rahul"))

str = "I am a software engineer."
print(str.split())  # return a list

# Capitalize()

blogHeading = "introduction to pYthon"
print(blogHeading.capitalize())    #First Character of the string to Capital and rest into small letter

#center()
str1 = "Welcome to the console"
print(len(str1))
print(str1.center(100))

# count()
str2 = 'Abracadabra'
print(str2.count('b'))
print(b.count('Nitish'))

#endswith()
str3 = "Welcome to the Console !!!"
print(str3.endswith("!!!"))

# we also check a 'str' between start and end position
print(str3.endswith('to', 4, 10))

# find()
str4 = "He's name is Dan. He is an honest man."
print(str4.find("is"))
print(str4.find("ishhh"))  # return -1 if not found
# print(str4.index("ishhh"))  # gives error when not found




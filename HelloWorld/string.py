course = "Python Programming"
message = """ 
Hi John,

This is Nitish from Tech Mahindra

How's everything going?
"""

print(message)
print(len(course))
print(course[0])
print(course[-1])
# Slicing
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

# Escape Sequences
# Backslash '\' we uses to escape a character after
# \ => escape character
# \" => escape sequence
company_name = "Tech \"Mahindra" 
print(company_name)

# \"
# \'
# \\ => \
# \n

# Formatted String

first = "Nitish"
last = "Kumar"

# full = first + " " + last
full = f"{first} {last} {len(first)} {2 + 2}"
print(full)

# String Methods
school_name = "   public school"
print(school_name.upper())
print(school_name.lower())
print(school_name.title())
print(school_name.strip())
print(school_name.lstrip())
print(school_name.rstrip())
print(school_name.find("ic"))  #return index
print(school_name.find("P"))
print(school_name.replace("p", "j"))
print("pub" in school_name)    #return boolean
print("swift" not in school_name)
# Logical Operator

# and
# or
# not

high_income = False
good_credit = True
student = False

# if high_income or good_credit:
#     print("Eligible for Loan")
# else:
#     print("Not Eligible for Loan")

if not student:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# In Pyhton the Boolean expression is short circuit

# eg. - if high_income and good_credit and not student:
#            print("Eligible")
# For AND operator
# if the first condition get False then it does not evalute what after it
# if every stat getting True then only it goes to the last and Check for Ture or False

# For OR operator
# If it gets TRUE in the first check then it does not check after
# Simply it returns TRUE



# ****************************************************************************************

# Chaining comparision operator
#  age should be between 18 and 65
age = 22
# if age >=18 and age < 65:
if 18 <= age < 65:
    print("Eligible")

# Similar to mathematics like 18 <= age < 65




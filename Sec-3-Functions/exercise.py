def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FIZZ BUZZ"
    if input % 3 == 0:
        return "FIZZ"
    if input % 5 == 0:
        return "BUZZ"
    else:
        return input



print(fizz_buzz(7))
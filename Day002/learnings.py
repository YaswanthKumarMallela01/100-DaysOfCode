print("Hippo"[0])  # Prints the 1st char of name
print("Hippo"[-1])  # Prints the last char of name

# Integers
print(123+456)
print(123_456_789)

# Float
print(3.143)

# Boolean
print(True)
print(False)

print(type("Hippo"))  # Prints the data type
print(type(int("123")))  # Although 123 is string it is converted into int because of type conversion

# PEMDAS
print(123 + 456)
print(456 - 123)
print(5 * 3)
print(5 / 3)
print(5 // 3)  # Removes the floating values and returns the int
print(5 ** 3)  # Exponent

# Round function
num = 58.7689258475
print(round(num))  # Rounds to nearest whole number
print(round(num, 2))

# f-String

score = 0
is_winning = False
print(f"Your score is {score} and you are winning: {is_winning}")
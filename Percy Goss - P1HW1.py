# Percy
# 11/02/2025 (11th of February, 2025)
# P1HW1
# A simple demonstration of formulas using inputs in Python

print()
print("-----Calculating Exponents-----")
print()
base = int(input("Enter an integer as the base value: "))
exp = int(input("Enter an integer as the exponent: "))
print()
if base ** exp > 10**3: exc = "!"
if base ** exp > 10**6: exc = "!!"
if base ** exp > 10**9: exc = "!!!"
if base ** exp < 1000: exc = "."
print(base, "raised to the power of", exp, "is", base ** exp, exc)
print()
print("----Addition and Subtraction----")
print()
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))
print()
print(num1, "+", num2, "-", num3, "is equal to", num1+num2-num3, ".")

# Percy Goss
# 04/03/2025 (4th of March, 2025)
# P3Lab
# Using logic and remainders to get multiple connected outputs from a single input

total = float(input("Enter the amount of money as a float: $"))
total = total * 100
print()

dollars = total // 100
if dollars == 1: print(f"{dollars:.0f} dollar")
if dollars > 1: print (f"{dollars:.0f} dollars")

remainder = total % 100

quarters = remainder // 25
if quarters == 1: print(f"{quarters:.0f} quarter")
if quarters > 1: print (f"{quarters:.0f} quarters")

remainder = remainder % 25

dimes = remainder // 10
if dimes == 1: print(f"{dimes:.0f} dime")
if dimes > 1: print (f"{dimes:.0f} dimes")

remainder = remainder % 10

nickels = remainder // 5
if nickels == 1: print(f"{nickels:.0f} nickel")
if nickels > 1: print (f"{nickels:.0f} nickels")

remainder = remainder % 5

pennies = remainder // 1
if pennies == 1: print(f"{pennies:.0f} penny")
if pennies > 1: print (f"{pennies:.0f} pennies")
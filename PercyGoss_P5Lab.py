# Percy Goss
# 08/04/2025 (8th of April, 2025)
# P5Lab
# Rehash of P3Lab, using random number generation and calculating change based on user input.

import random
owed = round(random.uniform(0.01, 100.00), 2)
print(f"You owe ${owed:.2f}")

paying = float(input('How much cash will you put in the self-checkout? $'))

owed = owed - paying
while owed > 0:
    if paying == 0:
        paying = float(input('You must pay for your goods. Please insert cash into the self-checkout. $'))
    else:
        paying = float(input(f'You still owe ${owed:.2f}. Please put in more cash. $'))
    owed = owed - paying
change = owed * (-1)
change = change * 100
print()

if change != 0:
    print("Your change is:")
dollars = change // 100
if dollars == 1: print(f"{dollars:.0f} dollar,")
if dollars > 1: print (f"{dollars:.0f} dollars,")

remainder = change % 100

quarters = remainder // 25
if quarters == 1: print(f"{quarters:.0f} quarter,")
if quarters > 1: print (f"{quarters:.0f} quarters,")

remainder = remainder % 25

dimes = remainder // 10
if dimes == 1: print(f"{dimes:.0f} dime,")
if dimes > 1: print (f"{dimes:.0f} dimes,")

remainder = remainder % 10

nickels = remainder // 5
if nickels == 1: print(f"{nickels:.0f} nickel,")
if nickels > 1: print (f"{nickels:.0f} nickels,")

remainder = remainder % 5

pennies = remainder // 1
if pennies == 1: print(f"and {pennies:.0f} penny.")
if pennies > 1: print (f"and {pennies:.0f} pennies.")
print()
print('Thank you for your purchase.')
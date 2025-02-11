# Percy
# 11/02/2025 (11th of February, 2025)
# P1HW1
# Another simple demonstration of Python's formula system, differently formatted.

print("This program displays your hypothetical travel expenses based on your own estimates. Basically, it's a glorified yet limited subtraction calculator.")
# I find transparency with your users to be very important, hence the tweaked heading.
print()
dest = input("Where are you going? ")
print()
budget = int(input("What is your budget? "))
print()
gas = int(input("How much do you think you'll spend on gas? "))
print()
stay = int(input("And about how much do you think you'll need to spend on accomodations or a hotel? "))
print()
food = int(input("Lastly, how much can you assume you'll need for food? "))
expenses = gas+stay+food
print()
print("----------Travel Expenses----------")
print("Location:", dest)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", stay)
print("Food:", food)
print()
print("Remaining Balance:", budget-expenses)

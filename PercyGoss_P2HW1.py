#Percy Goss
# 25/02/2025 (25th of February, 2025)
# P2HW1
# A much more neatly organized and well-formatted version of a prior program (P1HW2). Still just a glorified calculator though.

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
remainder = budget - expenses

print("\n------------Travel Expenses------------")
print(f"{'Location:':<20} {dest}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'Fuel':<20} ${gas:.2f}")
print(f"{'Accomodation':<20} ${stay:.2f}")
print(f"{'Food':<20} ${food:.2f}")
print("---------------------------------------")
print()
print(f"{'Remaining Balance:':<20} ${remainder:.2f}")
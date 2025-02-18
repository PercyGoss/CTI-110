# Percy Goss
# 18/02/2025 (Feb 18th, 2025)
# P2LAB2
# Working with dictionaries in Python, using certain car names as "keys" to provide their miles per gallon.

thisdict = {
    "Camero" : "18.21",
    "Prius" : "52.36",
    "Model S" : "110",
    "Silverado" : "26"
    }
x = thisdict.keys()
print(x,"\n")
key = input("Enter a vehicle to see it's MPG (Miles Per Gallon): ")
print()
print("The", key, "gets", thisdict[key], "MPG. \n")
MPG = float(thisdict[key])
miles = float(input("How many miles will you drive the " + key + "? "))
print()
gallons = miles / MPG
print(f"About {gallons:.2f} gallon(s) of gas are needed to drive the {key} {miles} mile(s).")

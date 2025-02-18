# Percy Goss
# 18/02/2025 (Feb 18th, 2025)
# P2LAB1
# Working with more complicated functions in Python, specifically regarding calculating circle dimensions ising pi, and importing "math" to do so.
import math
x = math.pi

rad = float(input("What is the radius of your circle? "))
dia = rad * 2
print()
print(f"The diameter of your circle is {dia}.") 
print()
circ = 2 * x * rad
print(f"The circumfrence of your circle is about {circ:.2f}.")
print()
area = x * math.pow(rad,2)
print(f"The area of your circle is about {area:.3f}.")

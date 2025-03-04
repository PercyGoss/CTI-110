#Percy Goss
# 25/02/2025 (25th of February, 2025)
# P2HW2
# More alignment practice, as well as working with an average and dependent variables.

M1 = float(input("Enter grade for Module 1: "))
M2 = float(input("Enter grade for Module 2: "))
M3 = float(input("Enter grade for Module 3: "))
M4 = float(input("Enter grade for Module 4: "))
M5 = float(input("Enter grade for Module 5: "))
M6 = float(input("Enter grade for Module 6: "))

grades = [M1, M2, M3, M4, M5, M6]
lowest = min(grades)
highest = max(grades)
total = sum(grades)
avg = total / len(grades)

print()

print("------------Results------------")
print(f"{'Lowest Grade:':<20} {lowest:.1f}")
print(f"{'Highest Grade:':<20} {highest:.1f}")
print(f"{'Sum of Grades':<20} {total:.1f}")
print(f"{'Average:':<20} {avg:.2f}")
print("-------------------------------")

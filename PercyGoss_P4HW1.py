#Percy Goss
#27/03/2025
#P4HW1
#A modified and more complex version of P2HW2, utilizing loops and including a deduction of the lowest score.

allscores = []
count = int(input('How many grades would you like to enter? '))
for score in range (1, count+1):
    program = 'yes'
    grade = float(input(f'Enter score #{score}: '))
    while (grade < 0 or grade > 100): 
        print("\nInvalid score detected.\nPlease enter a score between 0 and 100.")
        grade = float(input(f'Enter score #{score} again: '))
    allscores.append(grade)    
print()
lowest = min(allscores)
allscores.remove (lowest)

total = sum(allscores)
avg = total / len(allscores)

if avg >= 90: 
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

print("------------Results------------")
print(f"{'Lowest score':<20}: {lowest:.1f}")
print(f"{'Average':<20}: {avg:.2f}")
print(f"{'Modified list':<20}: {allscores}")
print(f"{'Final Grade':<20}: {grade}")
print("-------------------------------")

#The original program:
     
#M1 = float(input("Enter grade for Module 1: "))
#M2 = float(input("Enter grade for Module 2: "))
#M3 = float(input("Enter grade for Module 3: "))
#M4 = float(input("Enter grade for Module 4: "))
#M5 = float(input("Enter grade for Module 5: "))
#M6 = float(input("Enter grade for Module 6: "))

#grades = [M1, M2, M3, M4, M5, M6]
#lowest = min(grades)
#highest = max(grades)
#total = sum(grades)
#avg = total / len(grades)

#print()

#print("------------Results------------")
#print(f"{'Lowest Grade:':<20} {lowest:.1f}")
#print(f"{'Highest Grade:':<20} {highest:.1f}")
#print(f"{'Sum of Grades':<20} {total:.1f}")
#print(f"{'Average:':<20} {avg:.2f}")
#print("-------------------------------")
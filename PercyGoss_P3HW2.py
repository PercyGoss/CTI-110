# Percy Goss
# 06/03/2025 (6th of March, 2025)
# P3HW2
# Descision structure assesment

name = input("Enter employee's name: ")
hours = int(input("Enter number of hours worked: "))
wage = float(input("Enter employee's hourly wage: "))

ot = hours - 40
if ot < 0: ot = 0
if ot > 0: pay = wage * (hours - ot)
else: pay = wage * hours
otbonus = wage * 1.5
otpay = otbonus * ot
gross = pay + otpay

print("---------------------------------------")
print(f'Employee Name:  {name}')
print()
print(f'{'Hours Worked':<20}{'Hourly Wage':<20}{'Overtime':<15}{'Overtime Pay':<20}{'Regular Hours Pay':<25}{'Gross Pay':<15}')
print("----------------------------------------------------------------------------------------------------------------")
print(f'{hours:<20.1f}{wage:<20.1f}{ot:<15.1f}${otpay:<20.2f}${pay:<25.2f}${gross:<15.2f}')
